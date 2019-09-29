import sys
import time
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('file', type=argparse.FileType('r'), nargs='+', help='input a list of snplists from different GWAS batches')
parser.add_argument('-out',required=True, help='outfile a stringname with a suffix .txt')

def snp_extract(snplist):
	global snp_
	snp_={}
	for line in snplist:
		line_parse =  line.strip()
		if line_parse not in snp_:
			snp_[line_parse] = ''
	return(snp_)


all_snp=[]
dic_list =[]
args = parser.parse_args()
for n, value in enumerate(args.file):
	if n > 0:
		if value is not None:
			dic_list.append(snp_extract(snplist=value))
	else:
		all_snp.append(snp_extract(snplist=value))

n=0
missing =0
with open(args.out, 'w') as f_out:
	for key in all_snp[0].iterkeys():
		if all(key in d for d in dic_list):
			print key
			n += 1
			f_out.write(key+'\n')
		else:
			print 'to throw'
			missing += 1

print 'matched ', str(n), 'SNPS and Discarded other ', str(missing), 'SNPS' 
