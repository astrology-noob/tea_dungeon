# [6;7), [7;9), [10;11), [10;12), [8;10), [9;11), [6;8)
# [6;7), [6;8), [7;9), [8;10), [9;11), [10;11), [10;12)


def count_max_people(people_time: list):
    people_time.sort()
    count_time = [1, people_time[0]]

    for i in range(1, len(people_time)):
        if people_time[i][0] < count_time[1][1]:
            count_time[0] += 1

        else:
            count_time[1][0] = people_time[i][0]

    return count_time

people = [[6,7], [7,9], [10,11], [10,12], [8,10], [9,11], [6,8]]

print(count_max_people(people))