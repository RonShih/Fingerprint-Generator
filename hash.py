import glob
import hashlib
import sys
import os
import zlib

#CHUNKSIZE = int(input('Chunk size: ')) # a chunk size
LBA_SIZE = 512
input_address = "/mnt/c/Users/Ron/Desktop/input_linux"
output_address = "."
total_chunks_num = 0 
unique_chunks_num = 0 
LBA_num = 0
VBA_num = 0


def init_variable():
    global total_chunks_num
    global unique_chunks_num
    global LBA_num
    global VBA_num
    total_chunks_num = 0
    unique_chunks_num = 0
    LBA_num = 0
    VBA_num = 0

def show_dedupe_rate(total_chunks_num, unique_chunks_num, LBA_num, VBA_num): #calculate dedupe_rate
    print ("num of LBAs                    = ", LBA_num)
    print ("num of VBAs                    = ", VBA_num)
    ram_overhead = unique_chunks_num * 5 + LBA_num * 4 + VBA_num * 4
    print ("overall ram overhead           = ", ram_overhead, f"({ram_overhead / pow(2, 10)} KB)", f"({ram_overhead / pow(2, 20)} MB)")
    oob = unique_chunks_num * 28   #不太懂為什麼是28
    print ("overall OOB                    = ", oob, f"({oob / pow(2, 10)} KB)", f"({oob / pow(2, 20)} MB)")
    print ('Num of chunks                  = ', total_chunks_num)
    print ('Num of duplicate chunks        = ', total_chunks_num - unique_chunks_num)
    print ('Dedupe rate can be achieved to = ', (1.0 - (float(unique_chunks_num)/total_chunks_num))*100, '%')

def page_FP_4k_dedup():
    CHUNKSIZE = 4096
    global total_chunks_num
    global unique_chunks_num
    global LBA_num
    global VBA_num
    output_file_page_FP = open(os.path.join(output_address, 'fp_4k.txt'), 'w')
    hash_table = dict() #hash table (using dictionary)
    for filename in glob.glob(os.path.join(input_address, "*")): #input path
        print('Test FP:', filename, 'with chunk size', CHUNKSIZE)
        with open(filename, 'rb') as afile: #open each file
            for cur_chunk in iter(lambda: afile.read(CHUNKSIZE), b''): #for each chunk
                if len(cur_chunk) < CHUNKSIZE:
                    cur_chunk = cur_chunk.ljust(CHUNKSIZE, b'0') #如果page不滿一個page size就補零，我想說跟sketch那邊統一比較好
                LBA_num += 1
                hasher = hashlib.sha1(cur_chunk) #hash the chunk
                fingerprint = hasher.hexdigest()
                check_duplicate = fingerprint in hash_table #check if this fingerprint in hash_table
                if(check_duplicate == False):
                    hash_table[fingerprint] = 1 #insert reference = 1
                    unique_chunks_num += 1
                # else this is a duplicate chunk
                else:
                    if hash_table[fingerprint] == 1: #VBA not exist
                        VBA_num += 1
                    hash_table[fingerprint] += 1 #reference + 1
                total_chunks_num += 1
                output_file_page_FP.writelines(fingerprint + '\n') #write fp into output file

def page_FP_8k_dedup():
    CHUNKSIZE = 8192
    global total_chunks_num
    global unique_chunks_num
    global LBA_num
    global VBA_num
    output_file_page_FP = open(os.path.join(output_address, 'fp_8k.txt'), 'w')
    hash_table = dict() #hash table (using dictionary)
    for filename in glob.glob(os.path.join(input_address, "*")): #input path
        print('Test FP:', filename, 'with chunk size', CHUNKSIZE)
        with open(filename, 'rb') as afile: #open each file
            for cur_chunk in iter(lambda: afile.read(CHUNKSIZE), b''): #for each chunk
                if len(cur_chunk) < CHUNKSIZE:
                    cur_chunk = cur_chunk.ljust(CHUNKSIZE, b'0') #如果page不滿一個page size就補零，我想說跟sketch那邊統一比較好
                LBA_num += 1
                hasher = hashlib.sha1(cur_chunk) #hash the chunk
                fingerprint = hasher.hexdigest()
                check_duplicate = fingerprint in hash_table #check if this fingerprint in hash_table
                if(check_duplicate == False):
                    hash_table[fingerprint] = 1 #insert reference = 1
                    unique_chunks_num += 1
                # else this is a duplicate chunk
                else:
                    if hash_table[fingerprint] == 1: #VBA not exist
                        VBA_num += 1
                    hash_table[fingerprint] += 1 #reference + 1
                total_chunks_num += 1
                output_file_page_FP.writelines(fingerprint + '\n') #write fp into output file

def page_FP_16k_dedup():
    CHUNKSIZE = 16384
    global total_chunks_num
    global unique_chunks_num
    global LBA_num
    global VBA_num
    output_file_page_FP = open(os.path.join(output_address, 'fp_16k.txt'), 'w')
    hash_table = dict() #hash table (using dictionary)
    for filename in glob.glob(os.path.join(input_address, "*")): #input path
        print('Test FP:', filename, 'with chunk size', CHUNKSIZE)
        with open(filename, 'rb') as afile: #open each file
            for cur_chunk in iter(lambda: afile.read(CHUNKSIZE), b''): #for each chunk
                if len(cur_chunk) < CHUNKSIZE:
                    cur_chunk = cur_chunk.ljust(CHUNKSIZE, b'0') #如果page不滿一個page size就補零，我想說跟sketch那邊統一比較好
                LBA_num += 1
                hasher = hashlib.sha1(cur_chunk) #hash the chunk
                fingerprint = hasher.hexdigest()
                check_duplicate = fingerprint in hash_table #check if this fingerprint in hash_table
                if(check_duplicate == False):
                    hash_table[fingerprint] = 1 #insert reference = 1
                    unique_chunks_num += 1
                # else this is a duplicate chunk
                else:
                    if hash_table[fingerprint] == 1: #VBA not exist
                        VBA_num += 1
                    hash_table[fingerprint] += 1 #reference + 1
                total_chunks_num += 1
                output_file_page_FP.writelines(fingerprint + '\n') #write fp into output file

def page_FP_32k_dedup():
    CHUNKSIZE = 32768
    global total_chunks_num
    global unique_chunks_num
    global LBA_num
    global VBA_num
    output_file_page_FP = open(os.path.join(output_address, 'fp_32k.txt'), 'w')
    hash_table = dict() #hash table (using dictionary)
    for filename in glob.glob(os.path.join(input_address, "*")): #input path
        print('Test FP:', filename, 'with chunk size', CHUNKSIZE)
        with open(filename, 'rb') as afile: #open each file
            for cur_chunk in iter(lambda: afile.read(CHUNKSIZE), b''): #for each chunk
                if len(cur_chunk) < CHUNKSIZE:
                    cur_chunk = cur_chunk.ljust(CHUNKSIZE, b'0') #如果page不滿一個page size就補零，我想說跟sketch那邊統一比較好
                LBA_num += 1
                hasher = hashlib.sha1(cur_chunk) #hash the chunk
                fingerprint = hasher.hexdigest()
                check_duplicate = fingerprint in hash_table #check if this fingerprint in hash_table
                if(check_duplicate == False):
                    hash_table[fingerprint] = 1 #insert reference = 1
                    unique_chunks_num += 1
                # else this is a duplicate chunk
                else:
                    if hash_table[fingerprint] == 1: #VBA not exist
                        VBA_num += 1
                    hash_table[fingerprint] += 1 #reference + 1
                total_chunks_num += 1
                output_file_page_FP.writelines(fingerprint + '\n') #write fp into output file

def sector_FP_dedup():
    global total_chunks_num
    global unique_chunks_num
    global LBA_num
    global VBA_num
    output_file_sector_FP = open(os.path.join(output_address, 'fp_512B.txt'), 'w')
    hash_table = dict() #hash table (using dictionary)
    for filename in glob.glob(os.path.join(input_address, "*")): #input path
        print('Test FP:', filename, 'with chunk size', LBA_SIZE)
        with open(filename, 'rb') as afile: #open each file
            for cur_chunk in iter(lambda: afile.read(LBA_SIZE), b''): #for each chunk
                if len(cur_chunk) < LBA_SIZE:
                    cur_chunk = cur_chunk.ljust(LBA_SIZE, b'0') #如果page不滿一個page size就補零，我想說跟sketch那邊統一比較好
                LBA_num += 1
                hasher = hashlib.sha1(cur_chunk) #hash the chunk
                fingerprint = hasher.hexdigest()
                check_duplicate = fingerprint in hash_table #check if this fingerprint in hash_table
                if(check_duplicate == False):
                    hash_table[fingerprint] = 1 #insert reference = 1
                    unique_chunks_num += 1
                # else this is a duplicate chunk
                else:
                    if hash_table[fingerprint] == 1: #VBA not exist
                        VBA_num += 1
                    hash_table[fingerprint] += 1 #reference + 1
                total_chunks_num += 1
                output_file_sector_FP.writelines(fingerprint + '\n') #write fp into output file

def sector_CRC_generator():
    global total_chunks_num
    global unique_chunks_num
    global LBA_num
    global VBA_num
    output_file_sector_CRC = open(os.path.join(output_address, 'crc_512B.txt'), 'w')
    hash_table = dict() #hash table (using dictionary)
    for filename in glob.glob(os.path.join(input_address, "*")): #input path
        print('Generate CRC:', filename, 'with chunk size', LBA_SIZE)
        with open(filename, 'rb') as afile: #open each file
            for cur_chunk in iter(lambda: afile.read(LBA_SIZE), b''): #for each chunk
                if len(cur_chunk) < LBA_SIZE:
                    cur_chunk = cur_chunk.ljust(LBA_SIZE, b'0') #如果page不滿一個page size就補零，我想說跟sketch那邊統一比較好
                LBA_num += 1
                crc = zlib.crc32(cur_chunk)
                check_duplicate = crc in hash_table #check if this fingerprint in hash_table
                if(check_duplicate == False):
                    hash_table[crc] = 1 #insert reference = 1
                    unique_chunks_num += 1
                else:
                    if hash_table[crc] == 1: #VBA not exist
                        VBA_num += 1
                    hash_table[crc] += 1 #reference + 1
                total_chunks_num += 1
                output_file_sector_CRC.writelines(str(hex(crc)[2:]) + '\n') #write fp into output file

page_FP_4k_dedup()
show_dedupe_rate(total_chunks_num, unique_chunks_num, LBA_num, VBA_num)

init_variable()
page_FP_8k_dedup()
show_dedupe_rate(total_chunks_num, unique_chunks_num, LBA_num, VBA_num)

init_variable()
page_FP_16k_dedup()
show_dedupe_rate(total_chunks_num, unique_chunks_num, LBA_num, VBA_num)

init_variable()
page_FP_32k_dedup()
show_dedupe_rate(total_chunks_num, unique_chunks_num, LBA_num, VBA_num)

init_variable()
sector_FP_dedup()
show_dedupe_rate(total_chunks_num, unique_chunks_num, LBA_num, VBA_num)

init_variable()
sector_CRC_generator()
show_dedupe_rate(total_chunks_num, unique_chunks_num, LBA_num, VBA_num)