import sys
from pathlib import Path
from colorama import init, Fore, Style

init()

def print_directory_tree(directory: Path, prefix=""):
    for path in sorted(directory.iterdir()):
        if path.is_dir():
            print(f"{prefix}{Fore.BLUE}{path.name}{Style.RESET_ALL}/")
            print_directory_tree(path, prefix + "   ")
        else:
            print(f"{prefix}{Fore.GREEN}{path.name}{Style.RESET_ALL}")

def main():
    if len(sys.argv) <2:
        print("Specify the directory path as a command line argument.")
        return

    directory_path = Path(sys.argv[1])
    if not directory_path.exists():
        print("Error: Path does not exist.")
        return
    if not directory_path.is_dir():
        print("Error: This is not a directory.")  
        return

    print(f"\n Directory structure: {directory_path}\n")
    print_directory_tree(directory_path)

if __name__ == "__main__":
    main()              