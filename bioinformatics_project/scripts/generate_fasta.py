"""
This python script:
1) First generates a random DNA sequence (only one strand) and saves it as a string.
2) Then, it will format the sequence with 80 base per line.
3) Finally, it will save the sequence in random_sequence.fasta file.
"""

import random
import textwrap

def main():
    # List of DNA bases
    base_list = ["A", "T", "C", "G"]
    # Generate 1 million random bases (A,T,C,G)
    random_sequence =  ''.join(random.choices(base_list, k = 1000000))
    # Divide the sequence into lines of 80 bases in a line
    wrapped_sequence = textwrap.fill(random_sequence, width = 80)
    
    # Open the random_sequence.fasta file in a writable format
    with open('bioinformatics_project/data/random_sequence.fasta', 'w') as f:
        # save the sequence in the file
        print(wrapped_sequence,file = f)
    print("Random DNA sequence generated and saved to bioinformatics_project/data/random_sequence.fasta")

if __name__=="__main__":
    main()