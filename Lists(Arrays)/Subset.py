'''
Find All Subsets of a Set

(easy)

Problem Statement: Given a set with distinct elements, find all of its distinct subsets.

Example 1:
Input: [1, 3]
Output: [], [1], [3], [1,3]

Example 2:
Input: [1, 5, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]
'''

def find_subsets(nums):
    # create a subsets list
    subsets = []
    # append an empty set to the list
    subsets.append([])
    # loop through each element in nums
    for n in nums:
        # loop through each element in subset
        for i in range(len(subsets)):
            # copy the ith element and store it in temp list
            temp = subsets[i].copy()
            # append the current element to the temp list
            temp.append(n)
            # add the temp list to the subset
            subsets.append(temp)
    # return the subset
    return subsets

nums = [1, 3]
print(find_subsets(nums))
# Output: [[], [1], [3], [1, 3]]
nums2 = [1, 5, 3]
print(find_subsets(nums2))
# Output: [[], [1], [5], [1, 5], [3], [1, 3], [5, 3], [1, 5, 3]]

'''
Find Subset with Duplicate Values

(easy)

Problem Statement: Given a set of numbers that might contain duplicates, find all of 
its distinct subsets.

Example 1:
Input: [1, 3, 3]
Output: [], [1], [3], [1,3], [3,3], [1,3,3]

Example 2:
Input: [1, 5, 3, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3], [3,3], [1,3,3], [3,3,5], [1,5,3,3] 
'''

def find_subsets_with_duplicate(nums):
    # sort the nums list
    nums.sort()
    # create a subset list
    subsets = []
    # add an empty set
    subsets.append([])
    # initiate start and end variables
    start, end = 0, 0
    # loop through the nums list
    for i in range(len(nums)):
        # reset start to 0
        start = 0
        # if i is greater than 0 and the previous item is the same as the current item
        if i > 0 and nums[i] == nums[i - 1]:
            # then make start equal to end
            start = end
        # set end to the length of the subset list
        end = len(subsets)
        # loop from start to end
        for j in range(start, end):
            # copy the subset list into temp
            temp = subsets[j].copy()
            # add the current item to temp
            temp.append(nums[i])
            # append the temp set to the subset list
            subsets.append(temp)
    # return the subset list
    return subsets

nums = [1, 3, 3]
print(find_subsets_with_duplicate(nums))
# Output: [[], [1], [3], [1, 3], [3, 3], [1, 3, 3]]
nums2 = [1, 5, 3, 3]
print(find_subsets_with_duplicate(nums2))
# Output: [[], [1], [3], [1, 3], [3, 3], [1, 3, 3], [5], [1, 5], [3, 5], [1, 3, 5], [3, 3, 5], [1, 3, 3, 5]]

'''
String Permutation by Changing Case

(medium)

Problem Statement: Given a string, find all of its permutations preserving the character 
sequence but changing case.

Example 1:
Input: "ad52"
Output: "ad52", "Ad52", "aD52", "AD52" 

Example 2:
Input: "ab7c"
Output: "ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"
'''

def string_permutation(string):
    # create a permutations list
    permutations = []
    # add the initial string to the list
    permutations.append(string)
    # loop through each character in the string
    for i in range(len(string)):
        # if the character is alphabeticle
        if string[i].isalpha():
            # loop through the permutations list
            for j in range(len(permutations)):
                # copy the list into a temp list
                temp = list(permutations[j])
                # swap case with the current string
                temp[i] = temp[i].swapcase()
                # then add that string to the permutations list
                permutations.append(''.join(temp))
    # return the list
    return permutations

string = "ad52"
print(string_permutation(string))
# Output: ['ad52', 'Ad52', 'aD52', 'AD52']
string2 = "ab7c"
print(string_permutation(string2))
# Output: ['ab7c', 'Ab7c', 'aB7c', 'AB7c', 'ab7C', 'Ab7C', 'aB7C', 'AB7C']