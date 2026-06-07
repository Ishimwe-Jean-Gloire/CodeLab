with open("cowsignal.in", "r") as infile, open("cowsignal.out", "w") as outfile:
    M, N, K = map(int, infile.readline().split())   
    for _ in range(M):
        original_row = infile.readline().strip()
        stretched_row = ""
        for char in original_row:
            stretched_row += char * K
        for _ in range(K):
            outfile.write(stretched_row + '\n')