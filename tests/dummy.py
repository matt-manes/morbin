import argparse
import sys


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument("-t", "--text", type=str)

    args = parser.parse_args()

    return args


def main(args: argparse.Namespace):
    print(args.text, file=sys.stdout)


if __name__ == "__main__":
    main(get_args())
