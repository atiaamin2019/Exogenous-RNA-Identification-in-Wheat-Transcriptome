from collections import defaultdict

uniqseq = defaultdict(int)


infile = '/Users/aamin/Desktop/S002B4Btrimmed.fastq'
outfile = '/Users/aamin/Desktop/S002B4Btrimmed_uniq.tsv'

total_count = 0
unique_count = 0
cnt = 0
with open(infile, 'r') as file:
	for line in file:
		if cnt % 4 == 1:
			line = line.rstrip('\n')
		
			#print(line)
			uniqseq[line] +=1
			total_count +=1
		#if total_count == 10000:
		#	break
		cnt +=1

my_list = uniqseq.keys()
unique_count = len(my_list)

print('Total reads count:' + str(total_count))
print('Unique reads count:' + str(unique_count))

with open(outfile, 'w') as fout:
	for seq, count in uniqseq.items():
		fout.write("{}\t{}\n".format(seq, count))
