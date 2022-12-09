"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for item in items:
        i = str(item)
        if i in frequencies.keys():
            frequencies[i] += 1
        else:
            frequencies[i] = 1

    return frequencies
