from collections import defaultdict

bacteria = defaultdict(int)


infile = '/Users/aamin/Desktop/Library1.csv'
outfile= '/Users/aamin/Desktop/Library1_bac.csv'


total_count = 0

with open(infile, 'r') as file:
	for line in file:
		if line.startswith("Bacteria") and line not in my_list:
			line = str(line.rstrip('\n'))
			bacteria[line] +=1
			total_count += 1
			
my_list = bacteria.keys()


print('Total Bacterial reads count:' + str(total_count))


with open(outfile, 'w') as fout:
	for seq, count in bacteria.items():
		fout.write("{}\t{}\n".format(seq, count))


			






					

