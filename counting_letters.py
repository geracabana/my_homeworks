#Counting letters

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("main", help="count the ocurrences of each letter in the string you use here")
parser.add_argument("-v", "--vowels", help="count only the ocurrences of each vowl in the string you use here")
parser.add_argument("-c", "--consonants", help="count only the ocurrences of each consonant in the string you use here")

args = parser.parse_args()
count_letters = args.main

if args.vowels:
    vowels = "aeiouAEIOU"
    count = 0
    for char in count_letters:
        if char in vowels:
            count += 1
        print (count)

elif args.consonants:
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count2 = 0
    for chor in count_letters:
        if chor in consonants:
            count2 += 1
        print (count2)

else:
    string = count_letters.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    counts = {letter: string.len(letter) for letter in alphabet}
    sorted_counts = dict(sorted(counts.items()))
    for letter, count in sorted_counts.items():
        if count > 0:
            print(f"{letter}: {count}")







