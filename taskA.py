n, k = input().strip().split()
n, k = int(n), int(k)

if (n == 1) and (k == 1):
    print("Yes")
    print("1")
elif n >= k and (n*n % k == 0) and (k != 1):
    print("Yes")
    first_row = []
    for j in range(n//k):
        for i in range(1,k+1):
            first_row.append(i)
    second_row = first_row[1:] + [first_row[0]]
    for i in range(n):
        if i & 1 == 0:
            print(' '.join(map(str, first_row)))
        else:
            print(' '.join(map(str, second_row)))
else:
    print("No")