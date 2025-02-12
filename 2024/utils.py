import pathlib

data_dir = pathlib.Path(__file__).parent.resolve().joinpath("data")


def read_file(filename: str):
    with open(data_dir.joinpath(filename)) as f:
        for line in f:
            yield line
