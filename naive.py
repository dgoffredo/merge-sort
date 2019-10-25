
def merge_sort(items):
    # If `items` consisted of two sorted sublists, then we could merge them
    # together and have the solution.  So, let's do that.
    # First, though, an input list of length one or zero is already sorted.
    if len(items) < 2:
        return items

    pivot_index = len(items) // 2

    left = merge_sort(items[:pivot_index])
    right = merge_sort(items[pivot_index:])

    return merge(left, right)


def merge(left, right):
    # Return a new list that is the result of merging the specified sorted
    # lists `left` and `right`.
    # Let `i` be an index into `left` and `j` be an index into `right`.
    i = 0
    j = 0
    result = []

    # Note to self: current time 6:42

    while True:
        if i == len(left):
            # ? result.concat(some_list)
            result += right[j:]
            break

        if j == len(right):
            # ? result.concat(some_list)
            result += left[i:]
            break

        lefty = left[i]
        righty = right[j]

        if lefty < righty:
            result.append(lefty)
            i += 1
        else:
            result.append(righty)
            j += 1

    return result


if __name__ == '__main__':
    import json
    import sys
    
    numbers = json.load(sys.stdin)
    print(merge_sort(numbers))
    # Note to self: After playing with it a while, it's 6:51

    
# What is the complexity of this?
# The toplevel merge is O(n), but then for each n/2 we first invoke the same
# routine.  This means that C(n) = O(n) + 2 C(n/2).  With the base case that
# C(0) = 0, C(1) = 1.
#
# Guess that C(n) = n log n.  Put that in and you get
# n log n ?= n + n/2 + log n/2 = 3n/2 + log n/2 = 3n/2 + log n + log 1/2
# = O(n log n), yep.  Hm...
# "Master theorem (analysis of algorithms)"
# https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms)

# But wait, my reasoning is not sound.  We could try to plug in O(n) as well:
# n ?= n + 2*n/2 = 2n = O(n).  So, this is not how these things work.

# Out of curiosity, I'll write a program that plots values from the recurrence.
