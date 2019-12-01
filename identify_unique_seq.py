
infile = '/Users/aamin/Desktop/UQAM_Project/CodePractice/fake_file.fastq.txt'
my_list = []
total_count = 0
unique_count = 0
with open(infile, 'r') as file:
	for line in file:
		line = line.rstrip('\n')
		if '@' in line:
			total_count += 1
		if line not in my_list and line.isalpha():
			my_list.append(line)
			unique_count += 1
print(total_count)
print(unique_count)
print(my_list)
