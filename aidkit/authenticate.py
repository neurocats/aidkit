"""
Cli for executing models
"""
import argparse

from aidkit.data_access.authentication import authorize


def main():
    """Get arguments and execute performance measurement."""
    argument_parser = argparse.ArgumentParser(
        prog="Analysis",
        usage="python " + __file__,
        description='Authorize to the service.'
    )

    argument_parser.add_argument(
        '--url',
        help="Please specify the url to your aidkit, e.g. '\"http://<subdomain>.aidkit.ai\"'.",
        type=str
    )
    argument_parser.add_argument(
        '--token',
        help="Please authorize yourself with your aidkit token, e.g. \"dfvx47twnwo\"",
        type=str
    )
    args = argument_parser.parse_args()

    authorize(
        url=args.url,
        token=args.token
    )


if __name__ == "__main__":
    main()
    print("Authorized.")
