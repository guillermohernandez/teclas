import sys
from pathlib import Path

 
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    file_content = open_file(file_path)  
    print(file_content)  # Display the content


def open_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            file_contents = f.read()
            return file_contents

    except UnicodeDecodeError:
        # error handling
        print(f"check for utf8 error")
        with open(file_path, "r", encoding="utf-8", errors="replace") as f:
            file_contents = f.read()
            return file_contents

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        sys.exit(1)

 
if __name__ == "__main__":
    main()