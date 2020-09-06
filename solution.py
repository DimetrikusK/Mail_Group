import argparse
import json
import tempfile

parser = argparse.ArgumentParser()
parser.add_argument('--key')
key = parser.parse_args()
if key is not None:
    print("Aloha")
print('Error')