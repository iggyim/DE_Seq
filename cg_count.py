# replace 'sample.txt' with whatever string of nucleotide sequce 
# returns nucletide count and CG count of sequence 

with open('sample.txt') as sample:
    sample = sample.readline()

sample_list = list(sample)
#print(sample_list)

def cg_count(samp):
    count = 0
    for i in samp:
        if i == 'C' or i == 'G':
            count += 1
    outfile = open('cg_count.txt', "w")
    outfile.write(str(count)+"\n")
    outfile.write(str(len(samp)))
    outfile.close()

cg_count(sample_list)

# def splitting(x):
#     new = []
#     for i in x:
#         sub = i.split(',')
#         new.append(sub)
#     return(new)

# print(splitting(sample))

# def find_locations(sample, sequence):
#     outfile = open('locations.txt', 'w')

#     b = 0
#     for i in sample:
#         if i == query:
#             b += 1
#     print(b)
#     outfile.write()


#     while b<1000:
#         x = s.find(sequence, b)
#         a = str(x)+"-"+str(x+3)
#         outfile.write(a +'\n')
#         b += 150
#     outfile.close()

# sequence = 'CG'	
# print(find_locations(sample, sequence))



