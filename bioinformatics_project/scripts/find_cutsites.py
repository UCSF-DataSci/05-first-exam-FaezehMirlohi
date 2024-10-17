"""
This code gets two arguments; FASTA file path and cut site sequence, then,
1) Finds all occurrences of the cut site in the DNA sequence.
2) Finds all pairs of cut site locations that are 80,000-120,000 base pairs (80-120 kbp) apart.
3) Prints the total number of cut site pairs found and the positions of the first 5 pairs.
4) Saves a summary of the results (example below) in the results directory as "cutsite_summary.txt".
"""

import argparse
import re

def main(FASTA_path, cutsite):
    print('Analyzing cut site:', cutsite)

    # Remove the '|' symbol from the cut site sequence and uppercase it
    cut_seq = cutsite.replace("|", '').upper()

    # Open and process the FASTA file
    with open(FASTA_path, 'r') as f0:
        text = f0.read()
        sequence =  text.replace('\n', '').upper()  # Remove whitespaces and uppercase it

    # Count equals length of list with all found matched cut sites in the sequence
    cutsites_count = len(re.findall(cut_seq, sequence))

    # Find all cut sites in the sequence
    cut_indx = cutsite.find("|") # Index of cutting point ('|') in the cut sequence
    cut_index_list = []
    for site in re.finditer(cut_seq, sequence): # Iter among all cut sites
        cut_index_list.append(site.start() + cut_indx) # To find the index of the exact cut point ('|')


    # Find pairs of cut sites which are 80-120 kbp apart
    all_pairs_list = []
    for i in range(len(cut_index_list)):
        for j in range(i + 1, len(cut_index_list)): # For each cut site, loop over all subsequent cut sites within 80-120 kbs 
            if 80000 <= cut_index_list[j] - cut_index_list[i] <= 120000:
                all_pairs_list.append([cut_index_list[i], cut_index_list[j]]) # Append a pair list to list of all pairs

    # Print results
    if cutsites_count != 0:
        print(f"Total cut sites found: {cutsites_count}")
        print(f"Cut site pairs 80-120 kbp apart: {len(all_pairs_list)}")
        print('First 5 pairs:')
        for i in range(5):
            print(f"{i + 1}. {all_pairs_list[i][0]} - {all_pairs_list[i][1]}")

    # In case there is no cut sites found in the sequence
    else:
        print('No cut sites were found in this DNA sequence.')
    
    # Save the summary in "cutsite_summary.txt" file
    with open('bioinformatics_project/results/cutsite_summary.txt', 'w') as f1:
        f1.write(f"Analyzing '{cutsite}' cut site in DNA sequence from {FASTA_path} file:\n")
        if cutsites_count != 0: 
            f1.write(f"Total cut sites found: {cutsites_count}\n")
            f1.write(f"Cut site pairs 80-120 kbp apart: {len(all_pairs_list)}\n")
            f1.write('First 5 pairs:\n')
            for i in range(5):
                f1.write(f"{i + 1}. {all_pairs_list[i][0]} - {all_pairs_list[i][1]}\n")
        else:
            f1.write('No cut sites were found in this DNA sequence.')
    print("Summary saved in 'bioinformatics_project/results/cutsite_summary.txt'.")



if __name__=="__main__":
    # Command-line argument parsing
    parse = argparse.ArgumentParser()
    parse.add_argument('FASTA_path', help = 'FASTA file paththat contains the DNA strand')
    parse.add_argument('cutsite', help = 'Reference sequence of the cutting sites')

    # Parse and pass the arguments to the main function
    args = parse.parse_args()
    main(args.FASTA_path, args.cutsite)

