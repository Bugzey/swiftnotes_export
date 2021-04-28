#
#   Swiftnotes Export
#   Copyright (C) 2021  Radoslav Dimitrov
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
"""
Quick and dirty utility to export notes from Swiftnotes to a path of files

Usage:
    swiftnotes_export [options]

Options:
    -i, --input-file=PATH      Path to the Swoftnotes export JSON [default: swiftnotes_backup.json]
    -o, --output-dir=PATH      Target directory where notes should be exported as files 
                               [default: out]
    -e, --extension=EXTENSION  Extension of the output files. Assumes markdown [default: md]
    -h, --help                 Print this help text and exit
"""
from docopt import docopt
import os
import json
import sys

def parse_input(raw_args = sys.argv[1:]):
    result = docopt(doc = __doc__, argv = raw_args)
    return(result)

def check_io(target_file, target_dir):
    if not os.path.exists(target_file):
        raise FileNotFoundError("File: {} not found".format(target_file))

    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    elif not os.path.isdir(target_dir):
        raise NotADirectoryError("Target dir: {} not a directory".format(target_dir))
    
def export(target_file, target_dir, extension):
    with open(target_file) as cur_file:
        content = json.load(
            cur_file,
        )

    for note in content["notes"]:
        file_name = "{}.{}".format(
            note["title"].replace("/", ""),
            extension,
        )
        body = note["body"]

        output_path = os.path.join(
            target_dir,
            file_name,
        )

        with open(output_path, "w") as cur_file:
            cur_file.write(body)

def main(raw_args = sys.argv[1:]):
    args = parse_input(raw_args)

    target_file = args["--input-file"]
    target_dir = args["--output-dir"]
    extension = args["--extension"]

    check_io(target_file, target_dir)
    export(target_file, target_dir, extension)


if __name__ == "__main__":
    main()
