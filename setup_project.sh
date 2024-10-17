#!/bin/zsh
mkdir -p bioinformatics_project/data bioinformatics_project/scripts bioinformatics_project/results
touch bioinformatics_project/scripts/generate_fasta.py bioinformatics_project/scripts/dna_operations.py bioinformatics_project/scripts/find_cutsites.py
touch bioinformatics_project/results/cutsite_summary.txt
touch bioinformatics_project/data/random_sequence.fasta
touch bioinformatics_project/README.md
echo "This is a project consists of a shell script that have necessary commands to make a bioinformatics_project directory with 3 directories within it and each subdirectory has several files in it." > bioinformatics_project/README.md
