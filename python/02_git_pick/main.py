#!/usr/bin/env python3
# coding=utf-8
# noinspection PyUnresolvedReferences
import __init__

import os
import re
import sys

from util import *


def main(argv=None):
    input = 'input.txt'
    if argv is None:
        argv = sys.argv
    if len(argv) > 1:
        input = argv[1]
    id_list = []
    id_re = re.compile("\s([0-9a-f]{8,9})\s+-\s+(?!Merge)")
    with open(input, 'r') as fr:
        for line in fr:
            match = id_re.search(line)
            if match:
                commit_id = match.group(1)
                id_list.append(commit_id)
    id_list.reverse()
    command = ""
    first = True
    for cid in id_list:
        if first:
            first = False
        else:
            command += " && "
        command += "gitcp " + cid
    logger.i(__name__, command)
    pass


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt as _:
        logger.key_interrupt()
    finally:
        logger.i(__name__, 'FINISHED')
