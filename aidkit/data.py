"""
Cli for executing models
"""
import argparse

from aidkit.data_access.api import RESTApi


def main():
    """Get arguments and execute performance measurement."""
    argument_parser = argparse.ArgumentParser(
        prog="Data",
        usage="python " + __file__,
        description='Upload and list data.'
    )

    argument_parser.add_argument(
        '--file',
        help="Zip to upload. We expect a zip, containing a "
             "folder, that is named like the dataset should be called. "
             "This subfolder contains INPUT and OUTPUT folders that "
             "each contain csv files.",
        default=None,
        type=str
    )

    args = argument_parser.parse_args()

    api = RESTApi()

    if args.file is None:
        return api.list_data()
    else:
        return api.post_data(zip_path=args.file)


if __name__ == "__main__":
    print(main())
