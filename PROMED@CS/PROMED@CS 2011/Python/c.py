
n = int(input())

for n in range(n):
    map = {}

    while True:

        x, y = [int(x) for x in input().split(' ')]

        if x == 0 and y == 0:
            break
        else:

            # if map with key x isn't exist
            # then create a new one
            if x not in map:
                map[x] = []

            map[x].append(y)

    def solve():

        """
        solve() is a wrapper for avg() function
        """

        total = 0

        for x in map:
            for y in map:
                if x == y:
                    continue
                else:
                    total += avg(x, y)

        return total / len(map)

    def avg(src, dst, visited=[], count=0):

        """
        solve the problem recursively
        this function was meant to be called from solve() function
        """

        if dst in map[src]:
            return count + 1
        else:

            # find the shortest to the destination
            shortest = len(map)

            for directed in map[src]:

                # don't recurse if the node don't point to another nodes
                if directed not in map:
                    continue

                # don't follow previous path
                elif directed in visited:
                    continue

                else:
                    get = avg(directed, dst, visited + [src], count+1)

                    if get < shortest:
                        shortest = get

            return shortest


    print('Case ' + str(n+1) + ': ' + str(solve()) + ' degrees')
