def diff(file1, file2):
    with open(file1) as f1, open(file2) as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    maxlen = max(len(lines1), len(lines2))
    for i in range(maxlen):
        l1 = lines1[i].rstrip('\n') if i < len(lines1) else ''
        l2 = lines2[i].rstrip('\n') if i < len(lines2) else ''
        if l1 != l2:
            print(f"{i+1}c{i+1}")
            print(f"< {l1}")
            print("---")
            print(f"> {l2}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} file1 file2")
        exit(1)
    diff(sys.argv[1], sys.argv[2])
