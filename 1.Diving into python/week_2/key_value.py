import argparse
import json
import tempfile
import os

parser = argparse.ArgumentParser()
parser.add_argument('--key')
parser.add_argument('--val')
args = parser.parse_args()
c = dict()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
try:
    with open(storage_path, 'r') as f:
        c = json.load(f)
except:
    pass

try:
    if args.key and not args.val:
        with open(storage_path, 'r') as f:
            print(', '.join(c.get(args.key)))
except:
    pass

if args.key and args.val:
    znak = []
    with open(storage_path, 'w') as f:
        if args.key not in c:
            znak.append(args.val)
            c[args.key] = znak
        else:
            znak.extend(c[args.key])
            znak.append(args.val)
            c[args.key] = znak
        json.dump(c, f)
