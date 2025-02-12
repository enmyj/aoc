from datetime import datetime


def process_logs(logs: list[dict], levels: list[str]) -> list[str]:
    """
    filter by log level
    sort by timestamp in ascending order
    formats
    """
    filtered = sorted(
        [log for log in logs if log["level"] in levels],
        key=lambda x: x["timestamp"],
    )
    return [format(log) for log in filtered]


def format(log: dict) -> str:
    ts_formatted = datetime.strptime(log["timestamp"], "%Y-%m-%dT%H:%M:%SZ").strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    return """[{ts}] [{level}] {service}:{message}""".format(
        ts=ts_formatted,
        level=log["level"],
        message=log["message"],
        service=log["service"],
    )


if __name__ == "__main__":
    logs = [
        {
            "timestamp": "2025-02-11T14:36:22Z",
            "level": "INFO",
            "message": "User logged in",
            "service": "auth",
        },
        {
            "timestamp": "2025-02-11T14:35:22Z",
            "level": "ERROR",
            "message": "Something went wrong",
            "service": "auth",
        },
        {
            "timestamp": "2025-02-11T14:37:22Z",
            "level": "ERROR",
            "message": "Database connection failed",
            "service": "db",
        },
    ]

    print(process_logs(logs, ["ERROR", "DEBUG"]))
