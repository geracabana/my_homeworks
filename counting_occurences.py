#Counting occurences

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("x", help="count the ocurrences of this string you use here in the next string")
parser.add_argument("y", help="the string you use here")

args = parser.parse_args()
print (args.x.y)

counting = 0
p = {args.x}
if p in {args.y}:
    counting += 1
    print (f"string {args.x} occurred {counting} times in string {args.y}") 
else:
    print (f"string {args.x} occurred 0 times in string {args.y}")


