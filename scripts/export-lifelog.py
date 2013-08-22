#!/usr/bin/env python
# coding=utf-8
from dateutil import parser
from datetime import datetime
import subprocess


BEGIN = datetime(2013, 7, 24)
END = datetime(2013, 8, 28)


def export():
    command = [
        'lifelog',
        'bucket',
        'days',
        'minutes',
        '#typing'
    ]

    data = subprocess.check_output(command)

    rows = [row.split('\t') for row in data.splitlines()]

    for row in rows:
        row[0] = parser.parse(row[0])

    cleaned_rows = [row for row in rows
                    if row[0] >= BEGIN and row[0] <= END]

    for row in cleaned_rows:
        row[0] = row[0].date()

    cleaned_rows = ["\t".join([str(r) for r in row])
                    for row in cleaned_rows]

    print "\n".join(cleaned_rows)


if __name__ == '__main__':
    export()

