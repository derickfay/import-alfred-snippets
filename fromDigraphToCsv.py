#!/usr/bin/python3
import re
import os
import sys

from io import StringIO
from pathlib import Path
from typing import Optional, Tuple

from importSnippets import write_csv_to_alfred

digraph_pattern = re.compile(r'^digraph ([^ ]+) (\d+) " (.*)$')

def digraph_line_to_csv(line) -> Optional[Tuple[str, str, str]]:
    try:
        gr = digraph_pattern.match(line).groups()
    except AttributeError:
        return None

    keyword = gr[0] if len(gr[0]) == 2 else gr[0].replace('\\', '')
    snippet = chr(int(gr[1]))
    name = gr[2]

    return snippet, keyword, name

if __name__ == '__main__':
    currdir = f'{os.path.dirname(os.path.realpath(__file__))}'
    filename = sys.argv[1] if len(sys.argv) > 1 else Path(currdir, 'digraphs.vim').absolute()

    csv = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                processed = digraph_line_to_csv(line)

                if processed:
                    csv.append(processed)
    except FileNotFoundError as e:
        print(e)

    write_csv_to_alfred(StringIO('\n'.join(['\t'.join(entry) for entry in csv])))
