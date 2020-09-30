"""
Cli for executing models
"""
import argparse

from aidkit.data_access.api import RESTApi


def main():
    """Get arguments and execute performance measurement."""
    argument_parser = argparse.ArgumentParser(
        prog="Model",
        usage="python " + __file__,
        description='Upload and list models.'
    )

    argument_parser.add_argument(
        '--file',
        help="We expect a keras .h5 model that contains specific architectures.",
        default=None,
        type=str
    )

    args = argument_parser.parse_args()

    api = RESTApi()

    if args.file is None:
        return api.list_models()
    else:
        return api.post_model(model_path=args.file)


if __name__ == "__main__":
    print(main())
