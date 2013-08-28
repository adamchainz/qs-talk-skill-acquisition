#!/usr/bin/env python
# coding=utf-8
import subprocess
import sys
from dateutil import parser
from datetime import datetime, timedelta


BEGIN = datetime(2013, 7, 24)
END = datetime(2013, 8, 28)


def export(print_total):
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

    if not print_total:

        cleaned_rows = ["\t".join([str(r) for r in row])
                        for row in cleaned_rows]

        print "\n".join(cleaned_rows)

    else:
        total_minutes = sum([int(r[1]) for r in cleaned_rows])
        print timedelta(minutes=total_minutes)

if __name__ == '__main__':
    print_total = (len(sys.argv) > 1 and sys.argv[1] == '--total')
    export(print_total)

