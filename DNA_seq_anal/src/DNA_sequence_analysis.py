from Bio import SeqIO,pairwise2
from collections import Counter


# Read sequences from a FASTA file
def read_fasta(filename):
    sequences = []
    for seq_record in SeqIO.parse(filename, "fasta"):
        sequences.append(seq_record)
    return sequences

#count the frequency of each nucleotide (A, T, G, C) in the sequences
def nucleotide_frequency(sequences):
    for seq in sequences:
        counter = Counter(seq.seq)
        print(f"Nucleotide frequency for {seq.id}: {dict(counter)}")
        
    # Align the first two sequences
def align_sequences(seq1, seq2):
    alignments = pairwise2.align.globalxx(seq1, seq2)
    for alignment in alignments:
        print(pairwise2.format_alignment(*alignment))
        
def search_motif(sequences, motif):
    for seq in sequences:
        positions = [i for i in range(len(seq.seq)) if seq.seq[i:i+len(motif)] == motif]
        print(f"Motif '{motif}' found in {seq.id} at positions: {positions}")




