def merge_list_to_dict(list1, list2):
    return dict(zip(list1, list2))


res1 = merge_list_to_dict(['a', 'b', 'c'], [10, True, []])
print(res1)

res2 = merge_list_to_dict(['abc'], [{}, True, 100])
print(res2)

res3 = merge_list_to_dict(['a', True, 100], ['abc', 'haha'])
print(res3)