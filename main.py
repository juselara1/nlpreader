import sys, json, os, time

from argparse import ArgumentParser
from nlpreader import NLPReader
from nlpreader.configs import make_defaults
from os.path import expanduser

def make_parser():
    parser = ArgumentParser()
    parser.add_argument(
            "--text", type=str, default=None,
            help="Text to read"
            )
    return parser

def get_configs():
    home = expanduser("~")

    path = f"{home}/.config/nlpreader"

    if not os.path.exists(path):
        os.mkdir(path)
        make_defaults()
        print(f"Generated default configs at {path}")
        time.sleep(2)

    with open(f"{home}/.config/nlpreader/bindings.json") as f:
        bindings = json.load(f)

    with open(f"{home}/.config/nlpreader/colors.json") as f:
        colors = json.load(f)

    with open(f"{home}/.config/nlpreader/defaults.json") as f:
        defaults = json.load(f)

    return bindings, colors, defaults


if __name__=='__main__':
    parser = make_parser()
    args = parser.parse_args()

    bindings, colors, defaults = get_configs()

    reader = NLPReader(
            bindings, colors,
            defaults, args.text
            )

    reader.start()

    for line in sys.stdin:
        key = line.rstrip()
        reader.make_action(key)
        if reader.stop:
            break
