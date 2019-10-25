
def in_place_merge_sort(items, scratch=None):
    if scratch is None:
        scratch = [None for _ in items]

    if len(items) < 2:
        return

    # TODO: motivate the apparent backwardness
    _in_place_merge_sort_top_down(inway=scratch,
                                  outway=items,
                                  i=0,
                                  j=len(items))


def _in_place_merge_sort_top_down(inway, outway, i, j):
    assert len(inway) == len(outway)

    if j == i + 1:
        # TODO: the trick here is to make both sides have the value
        if inway[i] is None:
            inway[i] = outway[i]
        else:
            outway[i] = inway[i]

        return

    pivot = i + (j - i) // 2
    _in_place_merge_sort_top_down(outway, inway, i, pivot)
    _in_place_merge_sort_top_down(outway, inway, pivot, j)

    _merge(inway, outway, i, pivot, j)


def _merge(inway, outway, begin_index, pivot_index, end_index):
    i = begin_index  # in the input
    j = pivot_index  # in the input
    k = begin_index  # in the output

    while True:
        if i == pivot_index:
            while j != end_index:
                outway[k] = inway[j]
                j += 1
                k += 1
            return

        if j == end_index:
            while i != pivot_index:
                outway[k] = inway[i]
                i += 1
                k += 1
            return

        if inway[i] < inway[j]:
            outway[k] = inway[i]
            i += 1
            k += 1
        else:
            outway[k] = inway[j]
            j += 1
            k += 1


if __name__ == '__main__':
    import json
    import sys
    
    numbers = json.load(sys.stdin)
    in_place_merge_sort(numbers)
    print(numbers)
