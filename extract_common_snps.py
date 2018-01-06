import re
import subprocess
from subprocess import PIPE
import sys
import time
import argparse
parser = argparse.ArgumentParser()
#parser.add_argument('-1', '--list', nargs='+', help='<Required> Set flag', required=True)
parser.add_argument('file', type=argparse.FileType('r'), nargs='+')
def snp_extract(snplist):
	global snp_
	snp_={}
	for line in snplist:
		line_parse =  line.strip()
		if line_parse not in snp_:
			snp_[line_parse] = ''
	return(snp_)

#def main(sys.argv[1]):
#	pass
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
with open('SNPLIST_COMMON.txt', 'w') as f_out:
	for key in all_snp[0].iterkeys():
		if all(key in d for d in dic_list):
			print key
			n += 1
			f_out.write(key+'\n')
		else:
			print 'to throw'
			missing += 1

print 'matched ', str(n), 'SNPS and Discarded other ', str(missing), 'SNPS' 


#if key in dic_list[0] and dic_list[1] and dic_list[2]:
	#print 'yeay' 



#args_file=['CHB1_EXTRACT_P76.snplist',#'Axiom_550606_CHB1_merged_no68XYM_remR1_filterOUT.snplist']
#'CHB1_EXTRACT_P89.snplist', 
#'CHB1_EXTRACT_P94_95.snplist']

#def snp_extract(snplist):
#	global snp_
#	snp_={}
#	with open(snplist) as f_in:
#		for line in f_in:
#			line_parse =  line.strip()
#			if line_parse not in snp_:
#				snp_[line_parse] = ''
#	return(snp_)
