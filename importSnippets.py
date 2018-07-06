#!/usr/bin/python3

# importSnippets.py
#
# generates Alfred 3 json snippets from a csv file
#
# written for python 2.7.10

import csv
import json
import os
import sys
import binascii

from shutil import rmtree
from pathlib import Path
from zipfile import ZipFile

def write_csv_to_alfred(csvfile) -> None:
    currdir = os.path.dirname(os.path.realpath(__file__))
    builddir = Path(currdir, 'build')
    builddir.mkdir(exist_ok=True)

    reader = csv.reader(csvfile, delimiter='\t')

    for row in reader:
        uid = binascii.b2a_hex(os.urandom(15)).decode()
        output = json.dumps({
            'alfredsnippet' : {
                'snippet' : row[0],
                'uid': uid,
                'keyword' : row[1],
                'name' : row[2],
            }
        })

        output_file = builddir / Path(f'{row[2].replace("/", "or")} [{uid}].json')
        try:
            with open(output_file, 'w') as f:
                f.write(output)
        except OSError as e:
            print(e)

    zipname = f'{sys.argv[2]}.alfredsnippets' if len(sys.argv) > 2 else 'Snippets.alfredsnippets'
    if os.path.exists(zipname):
        os.remove(zipname)

    with ZipFile(zipname, 'w') as zf:
        for pth in builddir.iterdir():
            zf.write(pth, arcname=pth.name)

    try:
        rmtree(builddir)
    except FileNotFoundError:
        pass

if __name__ == '__main__':
    source_file = sys.argv[1] if len(sys.argv) > 1 else 'snippets.csv'

    try:
        with open (source_file, 'r') as csvfile:
            write_csv_to_alfred(csvfile)
    except FileNotFoundError as e:
        print(e)
