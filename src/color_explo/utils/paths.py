import pathlib


class PackagePaths:
    """Contains useful path for the package"""

    ROOT = pathlib.Path(__file__).resolve().parents[3].absolute()

    TEST = ROOT / "tests"

    DATA = pathlib.Path(__file__).resolve().parent.parent.absolute() / "data"

    APP_START = (
        pathlib.Path(__file__).resolve().parent.parent.absolute() / "st_app" / "main.py"
    )
