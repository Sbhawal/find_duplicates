import os, csv
from imohash import hashfile

hash_dict = {}

def calc_hashes(path):
    global hash_dict
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            hash = hashfile(file_path, hexdigest=True)
            if hash not in hash_dict:
                hash_dict[hash] = []
                hash_dict[hash].append(file_path)
            else:
                hash_dict[hash].append(file_path)


def export(path):
    global hash_dict
    with open(path, 'w') as f:
        writer = csv.writer(f)
        for key, value in hash_dict.items():
            writer.writerow([key, value])