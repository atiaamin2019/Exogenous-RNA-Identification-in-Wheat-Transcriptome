
infile = '/Users/aamin/Desktop/UQAM_Project/CodePractice/fake_file.fastq.txt'
my_list = []
total_count = 0
unique_count = 0
with open(infile, 'r') as file:
	for line in file:
		if '@' in line:
			total_count +=1
		elif '+' in line:
			pass
		elif '=' in line:
			pass
		elif line.rstrip('\n') not in my_list:
			my_list.append(line.rstrip('\n'))
			unique_count += 1
		
print(total_count)
print(unique_count)
print(my_list)
