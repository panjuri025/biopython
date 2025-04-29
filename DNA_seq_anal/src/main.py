
import sys
from DNA_sequence_analysis import read_fasta,nucleotide_frequency,align_sequences,search_motif

def main():
    # Load sequences
    sequences = read_fasta("data/fasta1.seq")
    
    # Print all sequences
    for seq in sequences:
        print(f"ID: {seq.id}, Sequence: {seq.seq}")

    # Perform nucleotide frequency analysis
    nucleotide_frequency(sequences)

    # Align the first two sequences
    align_sequences(sequences[0].seq, sequences[1].seq)

    # Search for a motif
    search_motif(sequences, "AGCT")

if __name__ == "__main__":
    main()



