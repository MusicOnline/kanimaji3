"""kanimaji3

Convert KanjiVG SVG into animated formats.

Usage:
    kanimaji3 <file> [-o FILE] [--format=FORMAT]
    kanimaji3 -h | --help
    kanimaji3 -V | --version

Options:
    -h --help               Show this message.
    -V --version            Show version.
    -o FILE --output=FILE   Specify output file.
    --format=FORMAT         Specify output format. [default: gif]
"""

from docopt import docopt, DocoptExit

from . import create_gif

if __name__ == "__main__":
    arguments: dict = docopt(__doc__, version="0.1.0")
    target_format = arguments["--format"].lower()
    if target_format not in ["gif"]:
        raise DocoptExit(f"{target_format} is not one of the recognized formats: 'gif'")
    if target_format == "gif":
        create_gif(arguments["<file>"], arguments["--output"])
