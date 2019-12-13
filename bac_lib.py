infile = '/Users/aamin/Desktop/Library1.csv'
outfile= '/Users/aamin/Desktop/Library1_bac.csv'

my_list = []
total_count = 0

with open(infile, 'r') as file:
	for line in file:
		line = str(line.rstrip('\n'))
		if line.startswith("Bacteria") and line not in my_list:
			total_count += 1
			my_list.append(line)

			
print('Total Bacterial Read Count:', total_count)
print(my_list)
with open(outfile, "w") as output:
	output.write(str(my_list))
