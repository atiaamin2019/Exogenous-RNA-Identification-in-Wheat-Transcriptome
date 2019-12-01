
infile = '/Users/aamin/Desktop/UQAM_Project/CodePractice/fake_file.fastq'
my_list = []
count = 1
with open (infile, 'r') as file:
	for line in file:
		if count>4:
			count = 1
		if count == 2:
			if line.rstrip('\n') not in my_list:
				my_list.append(line.rstrip('\n'))
		count += 1
print("Count:", count, my_list)
