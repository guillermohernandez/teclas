import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    file_content = get_book_text(file_path)
    print(file_content)
    

def get_book_text(file_path):
    with open(file_path) as f:
        book_contents = f.read()
        return book_contents


main()