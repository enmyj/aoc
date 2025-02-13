import json
from typing import Dict

category_map = {
    "electronics": "electronics",
    "audio": "electronics",
    "headphones": "electronics",
    "personal audio": "electronics",
}


class Standardized(Dict):
    name: str
    original_seller: str
    standardized_category: str
    price_usd: float
    original_format: str


def convert_to_usd(amount: float, currency: str) -> float:
    if currency == "EUR":
        return amount * 1.1
    elif currency == "USD":
        return amount
    else:
        raise Exception


def normalize_category(item: dict) -> str:
    category = (
        item.get("category") or item.get("product_type") or item.get("department")
    )
    if category is None:
        raise Exception("invalid category")

    match category:
        case str():
            category = category.lower()
        case list():
            category = category[0].lower()

    category = category.split("/")[0]

    return category_map.get(category, "uncategorized")


def normalize_price(item: dict):
    price = item.get("price_data") or item.get("pricing") or item.get("price_usd")
    if price is None:
        raise Exception("invalid price")

    match price:
        case int():
            price = float(price)
        case str():
            price = float(price)
        case dict():
            currency = price.get("currency")
            amount = price.get("amount")
            if not currency or not amount:
                raise Exception("invalid currency or amount")
            price = convert_to_usd(float(amount), currency)

    return price


def normalize(product: dict):
    s_category = normalize_category(product["item"])
    s_price = normalize_price(product["item"])

    return {
        "name": product["item"]["name"],
        "original_seller": product["seller"],
        "standardized_category": s_category or "n/a",
        "price_usd": s_price,
        "original_format": product,
    }


def standardize_products(input):
    standardized: list[Standardized] = []
    for product in input:
        s_product = normalize(product)
        standardized.append(s_product)

    return standardized


if __name__ == "__main__":
    input = [
        {
            "seller": "MarketHub",
            "item": {
                "name": "Wireless Headphones",
                "category": "ELECTRONICS/AUDIO/HEADPHONES",
                "price_data": {"amount": "89.99", "currency": "USD"},
            },
        },
        {
            "seller": "TechStore",
            "item": {
                "name": "Bluetooth Earbuds",
                "product_type": ["Electronics", "Personal Audio"],
                "pricing": 79.99,
            },
        },
        {
            "seller": "GlobalMart",
            "item": {
                "name": "Gaming Headset",
                "department": "electronics",
                "subdepartment": "gaming",
                "price_usd": 65,
            },
        },
    ]
    print(json.dumps(standardize_products(input), indent=4))
