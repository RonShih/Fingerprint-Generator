import glob
import hashlib
import sys
import os
CHUNKSIZE = 4096 # a chunk size
count = 0 #total file count
total_size_in_BYTE = 0 #total size of files
unique_size_in_BYTE = 0 #total files size without duplicated data chunk

def num_of_file(): #calculate the total file number
    count = 0
    for filename in glob.glob("input/*"):
        count += 1
    return count

def show_dedupe_rate(total_size_in_BYTE, unique_size_in_BYTE): #calculate dedupe_rate
    print ('total size         = ', total_size_in_BYTE)
    print ('not duplicate size = ', unique_size_in_BYTE)
    print ('duplicate size     = ', total_size_in_BYTE-unique_size_in_BYTE)
    print ('non duplicate rate = ', float(unique_size_in_BYTE)/total_size_in_BYTE)
    print ('dedupe_rate        = ', (1.0 - float(unique_size_in_BYTE)/total_size_in_BYTE))

output_file = open('output_fp.txt', 'w')

hash_table = dict() #hash table (using dictionary)
count = num_of_file()

for filename in glob.glob('input/*'):
    print('Test: ', filename, 'with chunk size', CHUNKSIZE)
    with open(filename, 'rb') as afile: #open each file
        for cur_chunk in iter(lambda: afile.read(CHUNKSIZE), b''):
            hasher = hashlib.sha1(cur_chunk) #hash the file
            fingerprint = hasher.hexdigest() #fingerprint is a hash value
            check_duplicate = fingerprint in hash_table #check if this fingerprint in hash_table
            if(check_duplicate == False):
                hash_table[fingerprint] = cur_chunk #insert it into dictionary
                unique_size_in_BYTE += len(cur_chunk)
            total_size_in_BYTE += len(cur_chunk)
            output_file.writelines(fingerprint + '\n') #write fp into output file
            afile.seek(CHUNKSIZE, 1) #move to next chunk

show_dedupe_rate(total_size_in_BYTE, unique_size_in_BYTE)

