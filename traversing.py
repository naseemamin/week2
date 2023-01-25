import os

def main():
    if os.path.isdir("C://Users//nasamin//Repos//coursera-de"):
        for root, directories, files in os.walk("C://Users//nasamin//Repos//coursera-de"):
            print(f"Root: {root}")
            print(f"Directories: {directories}")
            print(f"files {files}")
            for _file in files:
                absolute_path = os.path.join(root, _file)
                print(f"File path: {absolute_path}")
    else:
        print("path is not a directory")
        
if __name__ == '__main__':
    main()
