#Erasing letters

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("x", help="Original string")
parser.add_argument("y", help="Letters you want to delete on the original string")

args = parser.parse_args()
answer = args.x.y 

counts = 0
p = {args.y}

if p in {args.x}:
    output = {args.x} - p
    print(output)


