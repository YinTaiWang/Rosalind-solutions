#Transcribing DNA into RNA
#https://rosalind.info/problems/rna/


def to_rna(string):
    rna = []
    for i in string:
        if i == 'T':
            rna.append('U')
        else:
            rna.append(i)
    return rna

if __name__ == '__main__':
    with open('rosalind_dna.txt', 'r') as f:
        string = f.readline()
    trans = to_rna(string)
    RNA = ''.join(trans)
    print(RNA)