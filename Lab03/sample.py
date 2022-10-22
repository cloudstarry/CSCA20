times = [2, 3, 4, 5]
names = ['a', 'b', 'c', 'd']
input = 4

if input < times[0]:
    print('N/A')
else:
    mid = 0
    l = 0
    r = len(times) - 1
    index = -1

    while l < r - 1:
        mid = int(l + (r - l) / 2)
        if times[mid] == input:
            r = mid
        elif times[mid] < input:
            l = mid
        elif times[mid] > input:
            r = mid

    if times[r] < input:
        index = r + 1
    elif times[l] < input:
        index = l + 1

    if index == -1:
        print('N/A')
    else:
        print(sum(times[:index]) / index, names[:index])
        q = [x for x in times if x < input]
        print(sum(q) / len(q), names[:len(q)])
