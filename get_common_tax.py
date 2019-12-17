from collections import defaultdict
import glob

uniqseq = defaultdict(int)
outfile = "list_common_tax.txt"
for infile in glob.iglob("*.txt"):
	

#infile = 'S002B4Btrimmed.fastq'


	
	with open(infile, 'r') as file:
		for line in file:
			line = line.rstrip('\n')
			uniqseq[line] +=1

	my_list = uniqseq.keys()


	with open(outfile, 'w') as fout:
		for seq, count in uniqseq.items():
			if count == 4:
				fout.write("{}\t{}\n".format(seq, count))
