import os, csv
from imohash import hashfile

hash_dict = {}
cwd = os.getcwd()
total_files = 0
duplicates = 0

def calc_hashes(path):
    global hash_dict
    total_files = 0
    duplicates = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            hash = hashfile(file_path, hexdigest=True)
            if hash not in hash_dict:
                hash_dict[hash] = []
                hash_dict[hash].append(file_path)
            else:
                hash_dict[hash].append(file_path)
                duplicates += 1
            total_files += 1
    return total_files, duplicates


def get_space(size):
    if size < 1024:
        return "{} B".format(size)
    elif size < 1024*1024:
        return "{:.3f} KB".format(size/1024)
    elif size < 1024*1024*1024:
        return "{:.3f} MB".format(size/1024/1024)
    else:
        return "{:.3f} GB".format(size/1024/1024/1024)
    
    
    
def export(path):
    global hash_dict
    with open(path, 'w') as f:
        writer = csv.writer(f)
        for key, value in hash_dict.items():
            writer.writerow([key, value])
            
            
def display_record():
    global hash_dict
    total_space = 0
    print("\nDuplicate files:")
    for key, value in hash_dict.items():
        if len(value) > 1:
            print("\n---------------------------------------------------------------------------------------------------------------------")
            print("Duplicates found: {}".format(len(value)))
            print("Space consumed: {}".format(get_space(os.path.getsize(value[0])*len(value))))
            total_space += os.path.getsize(value[0])*len(value)-1
            for i in value:
                print("{}".format(cwd+i))
    print("\n---------------------------------------------------------------------------------------------------------------------")
    print("\nTOTAL SPACE CONSUMED BY DUPLICATES :", get_space(total_space))                


def find_duplicates(path):
    total_files, duplicates = calc_hashes(path)
    print("Number of files found: {}".format(total_files))
    print("Number of duplicates found: {}".format(duplicates))
    display_record()
    
    
    