import os
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_file>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    file_content = read_file_text(file_path)
    file_name = os.path.basename(file_path)
    print(f"opening {file_name}...")
    print(file_content)
    

def read_file_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def update_file_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents


main()