
table = ['MMM', 'GMM', 'MGM', 'MMG', 'MGG', 'GMG', 'GGM', 'GGG']

n = int(input())

for i in range(n):

    count = [0 for x in range(8)]
    str = input()

    for x in range(0, len(str), 3):
        cut = str[x:x+3]
        count[table.index(cut)] += 1

    # print the count
    for x in count:
        print(x, end='')

    print('')  # newline
