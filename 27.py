# def list_for_filter(list_to_filter, type_value):
#     filtered_list = []
#     for element in list_to_filter:
#         if type(element) == type_value:
#             filtered_list.append(element)
#     return filtered_list
#
#
# print(list_for_filter([10, 'abc', True, 25], int))
# print(list_for_filter([10, 'abc', True, 25], bool))

def filter_list(list_to_filter, value_type):
    def check_element_type(elem):
        return isinstance(elem, value_type)

    return list(filter(check_element_type, list_to_filter))


res = filter_list([1, 10, 'abc', 5.5], float)
print(res)

