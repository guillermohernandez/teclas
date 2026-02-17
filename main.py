import sys
from pathlib import Path

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_file>")
        sys.exit(1)
    
    #file_path = sys.argv[1]
    file_content = get_file_text(file_path)   
    file_path = Path("C:\\Users\\Memo\\Desktop\\docs\\1.txt")   

def get_file_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def edit_file_text(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        file_contents = f.read()
        return file_contents

if __name__ == "__main__":
    main()
