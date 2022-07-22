#Computing GC Content
#https://rosalind.info/problems/gc/

#ref:
#1. https://www.youtube.com/watch?v=aDvDfBVxcu0
#2. http://biopython.org/DIST/docs/tutorial/Tutorial.html#sec12

from Bio import SeqIO

max_seq_ID = None
max_gc_content = 0
for seq_record in SeqIO.parse('rosalind_gc.txt', 'fasta'):
    seq = str(seq_record.seq)
    seq_id = seq_record.id
    gc_content = round((seq.count('C') + seq.count('G')) / len(seq) * 100, 6)
    if gc_content > max_gc_content:
        max_gc_content = gc_content
        max_seq_ID = seq_id

print(max_seq_ID)
print(max_gc_content)



    