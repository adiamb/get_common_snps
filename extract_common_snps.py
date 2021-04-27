import argparse
from collections import defaultdict

def processSnplist(fileHandles):
    nFiles = len(fileHandles)
    snpDict = defaultdict(int)
    for fileC, snpFile in enumerate(fileHandles):
        for snp in snpFile:
            snpParse = snp.strip()
            snpDict[snpParse] += 1
    return(snpDict)

def processOut(out, snpDict, nFiles):
    snpCounter = 0
    with open(out, 'w') as outFile:
        for snp, val in snpDict.items():
            if val == nFiles:
                snpCounter += 1
                outFile.write(snp+'\n')
    if snpCounter > 0:
        print('MATCHED {} SNPS ACROSS {} BEDFILES'.format(snpCounter, nFiles))
    else:
        print('UNABLE TO FIND CONSENSUS AMONG THE SNPLISTS')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=argparse.FileType('r'), nargs='+', help='input a list of snplists from different GWAS batches')
    parser.add_argument('-out',required=True, help='outfile a stringname with a suffix .txt')
    args = parser.parse_args()
    fileHandles = args.file
    out = args.out
    nFiles = len(fileHandles)
    print('FOUND {} SNPLISTS'.format(nFiles))
    snpDict=processSnplist(fileHandles)
    processOut(out, snpDict, nFiles)

if __name__ == '__main__':main()
