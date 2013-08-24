#!/usr/bin/env python
# coding=utf-8
import json
import subprocess


def export():
    username = subprocess.check_output(['whoami']).strip()
    data_path = "/Users/%s/Library/Containers/com.type-fu.TypeFu/Data/Library/Application Support/Type Fu/storage.json" % username
    with open(data_path) as fh:
        data = json.load(fh)

    pairs = zip(data['speedHistory'], data['accuracyHistory'])

    for pair in pairs:
        print "\t".join(str(x) for x in pair)


if __name__ == '__main__':
    export()
