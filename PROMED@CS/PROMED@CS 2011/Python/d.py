
n = int(input())

for x in range(n):

    test = int(input())
    seven = '7'

    while (int(seven) % test) !=  0:
        seven += '7'

    print(len(seven))
