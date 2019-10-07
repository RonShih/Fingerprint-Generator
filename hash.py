import glob
import hashlib
import sys
import os
BLOCKSIZE = 4096 # a file size
count = 0 #total file count
total = 0 #total files size
unique = 0 #total files size without duplicated data chunk

def num_of_file(): #calculate the total file number
    count = 0
    for filename in glob.glob('bsplit.*'):
        if(filename != 'bsplit.c' and filename != 'bsplit.mk' and filename != 'bsplit.o'):
            count += 1
    return count

def show_dedupe_rate(total, unique): #calculate dedupe_rate
    print 'total size         = ', total
    print 'not duplicate size = ', unique
    print 'duplicate size     = ', total-unique
    print 'non duplicate rate = ', float(unique)/total
    print 'dedupe_rate        = ', (1.0 - float(unique)/total)



hash_table = dict() #hash table (using dictionary)
count = num_of_file()
filename = 'Small_file.dms'

for filename in glob.glob('Small_file*.dms'):
    print 'Test: ', filename, ' with blocksize ', BLOCKSIZE
    with open(filename, 'rb') as afile: #open each file
                buf = afile.read(BLOCKSIZE) #read each file
                count = 0
                while(len(buf) > 0):

                    hasher = hashlib.sha1(buf) #hash the file
                    fingerprint = hasher.hexdigest() #fingerprint is a hash value

                    check_duplicate = fingerprint in hash_table #check if this fingerprint in hash_table

                    #file_size = os.path.getsize(filename) #get the size of each file
                    #print file_size
                    if(check_duplicate == False):
                        hash_table[fingerprint] = filename #insert it into dictionary
                        #unique += file_size
                        unique += len(buf)
                    #total += file_size
                    total += len(buf)
                    
                    #if(hasher.hexdigest() == '193b92bdedac1894a3ffc56d7b7fd308afb00d63' or hasher.hexdigest() == '19a73ebc32c1e076eac457cf1f9c8d6dde6e8c30'):
                        #print hasher.hexdigest()
                    buf = afile.read(BLOCKSIZE)
                    count += 1


show_dedupe_rate(total, unique)

