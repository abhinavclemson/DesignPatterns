class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[{0}, {1}]".format(self.start, self.end))



def merge(intervals):

    if len(intervals)<1:
        #the intervals list is empty
        return []

    merged = []
    #Here we are sorting the intervals with starting time of each interval
    intervals.sort(key=lambda x: x.start)

    runningStart = intervals[0].start
    runningEnd = intervals[0].end

    for i in range(1, len(intervals)):
        currentStart, currentEnd = intervals[i].start, intervals[i].end

        #case 1:
        if runningEnd<currentStart:
            merged.append(Interval(runningStart, runningEnd))
            runningStart = currentStart
            runningEnd = currentEnd

        #case 2: There is an overlapping
        elif runningEnd>=currentStart:
            runningStart = min(runningStart, currentStart) #Not required
            runningEnd = max(runningEnd, currentEnd)


    merged.append(Interval(runningStart, runningEnd))





    return merged




def main():
    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
        i.print_interval()
    print()

main()