import os
from bruteforce import bruteforce
from optimized import optimized

if __name__ == "__main__":
    file_list = os.listdir('data')
    print("List of files in the data directory:", end='\n\n')

    for file in file_list:
        print(f"[{file_list.index(file) + 1}] {file}")

    print("\nSelect file to process: ", end='')

    file_selected = ''
    try:
        file_selected = file_list[int(input()) - 1]
    except:
        print("That item does not exist, ending program")
        raise SystemExit

    print("\n[1] Bruteforce")
    print("[2] Optimized")
    print(f"\nSelect algorithm to use on file {file_selected}: ", end='')

    match input():
        case "1":
            bruteforce(file_selected)
        case "2":
            optimized(file_selected)
        case _:
            print("Invalid parameter, ending program")
            raise SystemExit
