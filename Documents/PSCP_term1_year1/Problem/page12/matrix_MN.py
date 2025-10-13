"""Matrix_MN"""

def main():
    """Main"""
    m = int(input())
    n = int(input())
    matrix = []
    pre_matrix = []
    for _ in range(m):
        for _ in range(n):
            pre_matrix.append(int(input()))
        matrix.append(pre_matrix)
        pre_matrix = []
    for i in range(m):
        for j in range(n):
            print(matrix[i][j], end=" " * (j + 1 != n))
        print()

main()
