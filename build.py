#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
import json

BASE_URI = 'https://aidbox.github.io/notebooks'

def parse_notebook(file, base):
    with open(f"{base}/{file}", 'r') as f:
        notebook = json.load(f)
        name = notebook['name'] if 'name' in notebook else None
        description = notebook['description'] if 'description' in notebook else None
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
    files = list(os.listdir(base))
    notebooks = [parse_notebook(file, base) for file in files]
    return {'version': 1,
            'notebooks': notebooks}


def main():
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'w') as f:
            json.dump(parse_files('./notebooks'), f)
    else:
        print(json.dumps(parse_files('./notebooks')))

if __name__ == '__main__':
    main()
