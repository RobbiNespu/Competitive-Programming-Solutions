
n = int(input())

for n in range(n):

    num = input().split(' ')
    start_hour, end_hour = int(num[0]), int(num[2])
    start_mins, end_mins = int(num[1]), int(num[3])

    sm_hand = start_mins / 60 * 12
    em_hand = end_mins / 60 * 12

    if start_hour == 12:
        start_hour = 0

    if end_hour == 12:
        end_hour = 0

    total = 0

    if start_hour == end_hour and sm_hand < em_hand:
        if sm_hand < start_hour and em_hand > end_hour:
            total += 1
    else:

        if sm_hand < start_hour:
            total += 1

        if em_hand > end_hour:
            total += 1

        if start_hour < end_hour:
            total += end_hour - start_hour - 1
        else:
            # -1 at the end of equation is because in 12 hour hand, no clashing
            # between minute hand and hour hand occured
            total += (12 - start_hour - 1) + end_hour - 1

    print(num[0] + ':' + num[1],  # start time
          num[2] + ':' + num[3],  # end time
          total)
