# Counting DNA Nucleotides
# https://rosalind.info/problems/dna/

def counting(string):
    return string.count('A'), string.count('C'), string.count('G'), string.count('T')

def source():
    while True:
        source = input('string/file: ')
        if source == 'string':
            string = input('Please type the string: ')
        elif source == 'file':
            filename = input('file name: ')
            with open(f'{filename}', 'r') as f:
                string = f.readline()
        else:
            print('Please type string/file.')
        return string

if __name__ == '__main__':
    string = source()
    results = counting(string)
    print (results)