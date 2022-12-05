import glob
import hashlib
import sys
import os
CHUNKSIZE = 512 # a chunk size
total_chunks_num = 0 
unique_chunks_num = 0 

def show_dedupe_rate(total_chunks_num, unique_chunks_num): #calculate dedupe_rate
    print ('Num of chunks                  = ', total_chunks_num)
    print ('Num of duplicate chunks        = ', total_chunks_num - unique_chunks_num)
    print ('Dedupe rate can be achieved to = ', (1.0 - (float(unique_chunks_num)/total_chunks_num))*100, '%')

output_file = open('/mnt/c/Users/Ron/Desktop/output.txt', 'w')

hash_table = dict() #hash table (using dictionary)

for filename in glob.glob("/mnt/c/Users/Ron/Desktop/Input/*"): #input path
    print('Test:', filename, 'with chunk size', CHUNKSIZE)
    with open(filename, 'rb') as afile: #open each file
        for cur_chunk in iter(lambda: afile.read(CHUNKSIZE), b''): #for each chunk
            hasher = hashlib.sha1(cur_chunk) #hash the chunk
            fingerprint = hasher.hexdigest()
            check_duplicate = fingerprint in hash_table #check if this fingerprint in hash_table
            if(check_duplicate == False):
                hash_table[fingerprint] = cur_chunk #insert it into dictionary
                unique_chunks_num += 1
            # else this is a duplicate chunk
            total_chunks_num += 1
            output_file.writelines(fingerprint + '\n') #write fp into output file
            afile.seek(CHUNKSIZE, 1) #move to next chunk

show_dedupe_rate(total_chunks_num, unique_chunks_num)

