"""
This code accepts a DNA sequence as a command-line argument and then returns:
1) The original DNA sequence,
2) Complement strand of the DNA sequence,
3) The reverse of the DNA sequence,
4) The reverse complement of the DNA sequence.
"""

import argparse

def main(sequence):
    print(f"Orginal sequence: {sequence}")
    print(f"Complement: {complement(sequence)}")
    print(f"Reverse: {reverse(sequence)}")
    print(f"Reverse complement: {reverse_complement(sequence)}")

def complement(sequence):
    # Create a translation table using maketrans()
    base_complement = str.maketrans('ATCGatcg', 'TAGCtagc')
    # Make complement string by adding complement of each base of original strand 
    complement_seq = sequence.translate(base_complement)
    return complement_seq

def reverse(sequence):
    # Reverse the string
    return sequence[::-1]

def reverse_complement(sequence):
    # Reverse the complement sequence
    return reverse(complement(sequence))

if __name__=="__main__":
    # Command-line argument parsing
    parser = argparse.ArgumentParser()
    parser.add_argument('sequence', help = 'The DNA strand sequence')

    # Parse and pass the argument to the main function
    args = parser.parse_args()
    main(args.sequence)
