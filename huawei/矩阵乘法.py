while True:
    try:
        x = int(input())
        y = int(input())
        z = int(input())
        A = []
        B = []
        C = [[0 for _ in range(z)] for _ in range(x)]
        for _ in range(x):
            A.append(list(map(int, input().split())))
        for _ in range(y):
            B.append(list(map(int, input().split())))
        for i in range(x):
            for j in range(z):
                for k in range(y):
                    C[i][j] += A[i][k] * B[k][j]
        for row in C:
            for r in row:
                print(r, end=' ')
            print()
    except:
        break
