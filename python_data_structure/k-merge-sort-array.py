# -*- coding: utf-8 -*-


import heapq



def sort_lists(*some_arrays):
    """

    :param some_arrays:
    :return:
    """
    hq_index = {}
    hq_num = []
    for loc, array in enumerate(some_arrays):
        one = array.pop(0)
        heapq.heappush(hq_num, one)
        hq_index.setdefault(one, []).append(loc)
    result = list()

    while hq_index:
        item = hq_num.pop(0)
        next_loc = hq_index[item].pop(0)
        if some_arrays[next_loc]:
            new_item = some_arrays[next_loc].pop(0)
            heapq.heappush(hq_num, new_item)
            hq_index.setdefault(new_item, []).append(next_loc)
        if not hq_index[item]:
            hq_index.pop(item)
        result.append(item)
    return result


ret = sort_lists([4, 5, 9], [10, 11], [1, 3, 22, 100])
print(ret)

