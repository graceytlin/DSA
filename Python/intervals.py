def insert(intervals, newInterval):
    result = []

    for i in range(len(intervals)):
        if newInterval[1] < intervals[i][0]:
            result.append(newInterval)
            return result + intervals[i:]
        elif newInterval[0] > intervals[i][1]:
            result.append(intervals[i])
        else:
            newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]

    result.append(newInterval)

    return result


print(insert([[1, 2], [3, 5]], [2, 3]) == [[1, 5]])
