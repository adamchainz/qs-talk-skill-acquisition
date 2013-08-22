#!/usr/bin/env python
# coding=utf-8
from datetime import datetime
import subprocess


DB_LOCATION = "/Applications/Amphetype.app/Contents/Resources/chainz.db"

# I just care about my performance on the test set of texts - the first set I
# put in.
SOURCE_ID = 1


def export():
    sql = "SELECT w real, wpm real, accuracy real FROM result WHERE source=%s;" % SOURCE_ID
    command = [
        'sqlite3',
        '-batch',
        DB_LOCATION,
        sql
    ]

    data = subprocess.check_output(command)

    rows = [row.split('|') for row in data.splitlines()]
    cleaned_rows = []

    for row in rows:
        row[0] = datetime.fromtimestamp(float(row[0])).isoformat()
        cleaned_rows.append("\t".join(row))

    print "\n".join(cleaned_rows)


if __name__ == '__main__':
    export()
