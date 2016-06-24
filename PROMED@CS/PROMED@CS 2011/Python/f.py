
n = int(input())

for x in range(n):

    max, min, gap, last = 0, 50, 0, 0

    for i, n in enumerate(sorted(input().split(' ')[1:])):
        n = int(n)

        if n > max:
            max = n
        if n < min:
            min = n
        if i > 0:
            if abs(n - last) > gap:
                gap = abs(n - last)

        last = n

    print('Class', x+1)
    print('Max ' + str(max) + ', Min ' + str(min) + ', Largest gap ' + str(gap))
