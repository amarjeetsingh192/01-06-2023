list_a = [True, True]
is_all_true = all(list_a)
print(is_all_true)


set = {}
is_all_true = all(set)
print(is_all_true)


is_true_in_list = all([1,2,3,4,0])
is_true_in_set = all({True,"ram",2})
is_true_in_tuple = all((" ", "hello","python"))
print(is_true_in_list)
print(is_true_in_set)
print(is_true_in_tuple)