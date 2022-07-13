'''
Merge Intervals

(medium)

Problem Statement: Given a set of time intervals in any order, merge all overlapping intervals 
into one and output the result which should have only mutually exclusive intervals.

Example 1:
Input: height = [[1, 3], [2, 4], [6, 8], [9, 10]]
Output: [1, 4], [6, 8], [9, 10]
Explanation: Given intervals: [1,3],[2,4],[6,8],[9,10], we have only two overlapping intervals 
here,[1,3] and [2,4]. Therefore we will merge these two and return [1,4],[6,8], [9,10].

Example 2:
Input: intervals = [[6, 8], [1, 9], [2, 4], [4, 7]]
Output: [1, 9]
'''

def mergeIntervals(intervals):
    # sort the list
    intervals.sort()
    # create a stack
    stack = []
    # push the first interval to the stack
    stack.append(intervals[0])
    # loop through the array
    for i in intervals[1:]:
        print(f"{stack[-1][0]} <=  {i[0]} <= {stack[-1][-1]}")
        # if the first element of the second interval is between both elements of the first interval
        if stack[-1][0] <= i[0] <= stack[-1][-1]:
            # add the bigger element two second elements to the first interval
            stack[-1][-1] = max(stack[-1][-1], i[-1])
        else:
            # otherwise add the interval to the stack
            stack.append(i)
    # return the stack
    return stack

intervals1 = [[1, 3], [2, 4], [6, 8], [9, 10]]
print(mergeIntervals(intervals1))
# Output: [[1, 4], [6, 8], [9, 10]]
intervals2 = [[6, 8], [1, 9], [2, 4], [4, 7]]
print(mergeIntervals(intervals2))
# Output: [[1, 9]]