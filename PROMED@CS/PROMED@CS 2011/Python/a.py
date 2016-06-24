
row = int(input())  # get number of row from user

for n in range(row):

    # [:-2] is to remove the ' ;' at the end of each string
    str = input()[:-2].split(' ')

    for x in str:
        print('*' * len(x))

    print('')  # print newline after each test case
