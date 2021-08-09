#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
import json

BASE_URI = 'https://aidbox.github.io/notebooks'

def parse_notebook(file, base):
    with open(f"{base}/{file}", 'r') as f:
        j = json.load(f)
        res = {}
        name = j['name'] if 'name' in j else None
        description = j['description'] if 'description' in j else None
        uri = f"{BASE_URI}/{file}"
        
        return {
            'name': name,
            'description': description,
            'source': {
                'type': 'uri',
                'path': uri
            },
            'tags': {
                'type': 'string_array',
                'value': ['official']
            }
        }


def parse_files(base):
    lst = list(os.listdir(base))
    notebooks = [parse_notebook(file, base) for file in lst]
    return {'version': 1,
            'notebooks': notebooks}


def main():
    lst = list(os.listdir('./notebooks'))
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'w') as f:
            json.dump(parse_files('./notebooks'), f)
    else:
        print(json.dumps(parse_files('./notebooks')))

if __name__ == '__main__':
    main()
