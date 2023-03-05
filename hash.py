import glob
import hashlib
import sys
import os
import zlib

CHUNKSIZE = int(input('Chunk size: ')) # a chunk size
LBA_SIZE = 512
total_chunks_num = 0 
unique_chunks_num = 0 

def show_dedupe_rate(total_chunks_num, unique_chunks_num): #calculate dedupe_rate
    print ('Num of chunks                  = ', total_chunks_num)
    print ('Num of duplicate chunks        = ', total_chunks_num - unique_chunks_num)
    print ('Dedupe rate can be achieved to = ', (1.0 - (float(unique_chunks_num)/total_chunks_num))*100, '%')

def page_FP_dedup():
    global total_chunks_num
    global unique_chunks_num
    output_file_page_FP = open('/mnt/c/Users/Ron/Desktop/page_fp_output.txt', 'w')
    hash_table = dict() #hash table (using dictionary)
    for filename in glob.glob("/mnt/c/Users/Ron/Desktop/Input/*"): #input path
        print('Test FP:', filename, 'with chunk size', CHUNKSIZE)
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
                output_file_page_FP.writelines(fingerprint + '\n') #write fp into output file
                afile.seek(CHUNKSIZE, 1) #move to next chunk

def sector_FP_dedup():
    global total_chunks_num
    global unique_chunks_num
    output_file_sector_FP = open('/mnt/c/Users/Ron/Desktop/sector_fp_output.txt', 'w')
    hash_table = dict() #hash table (using dictionary)
    for filename in glob.glob("/mnt/c/Users/Ron/Desktop/Input/*"): #input path
        print('Test FP:', filename, 'with chunk size', LBA_SIZE)
        with open(filename, 'rb') as afile: #open each file
            for cur_chunk in iter(lambda: afile.read(LBA_SIZE), b''): #for each chunk
                hasher = hashlib.sha1(cur_chunk) #hash the chunk
                fingerprint = hasher.hexdigest()
                check_duplicate = fingerprint in hash_table #check if this fingerprint in hash_table
                if(check_duplicate == False):
                    hash_table[fingerprint] = cur_chunk #insert it into dictionary
                    unique_chunks_num += 1
                # else this is a duplicate chunk
                total_chunks_num += 1
                output_file_sector_FP.writelines(fingerprint + '\n') #write fp into output file
                afile.seek(LBA_SIZE, 1) #move to next chunk

def sector_CRC_generator():
    output_file_sector_CRC = open('/mnt/c/Users/Ron/Desktop/sector_crc_output.txt', 'w')
    for filename in glob.glob("/mnt/c/Users/Ron/Desktop/Input/*"): #input path
        print('Generate CRC:', filename, 'with chunk size', LBA_SIZE)
        with open(filename, 'rb') as afile: #open each file
            for cur_chunk in iter(lambda: afile.read(LBA_SIZE), b''): #for each chunk
                crc = zlib.crc32(cur_chunk)
                output_file_sector_CRC.writelines(str(hex(crc)[2:]) + '\n') #write fp into output file
                afile.seek(LBA_SIZE, 1) #move to next chunk

page_FP_dedup()
print(total_chunks_num, unique_chunks_num)
show_dedupe_rate(total_chunks_num, unique_chunks_num)
total_chunks_num = 0
unique_chunks_num = 0
sector_FP_dedup()
show_dedupe_rate(total_chunks_num, unique_chunks_num)
sector_CRC_generator()