import hashlib

def main():
    with open("MD5_Hashes.txt", 'w') as f:
        print("[+] File created")
        print("[+] File name - MD5_Hashes.txt")
        for i in range(-100, 1):
            hash_object = hashlib.md5(str(i).encode())
            hash_value = hash_object.hexdigest()
            f.write(hash_value+'\n')
    print("[+] Successfully completed. Please check the file.")

if __name__ == "__main__":
    main()