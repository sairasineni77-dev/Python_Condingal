nest_tup = (1, 2, ('a', 'b'), [4,5,'nesting'])

print(nest_tup)
print("The value at index 2 in tuple", nest_tup[2])
val_index_2 = nest_tup[2]
val_a = val_index_2[0]
val_b = nest_tup[2][1]
print("The value of a is", val_a)
print("The value of b is", val_b)
# access elements of nested tuple

print(nest_tup[2])

print(nest_tup[-1][-1])
nest_list = [[1, 2], [3.8, 9.2], ["a", "b"], ("Hello", "World")]
val_2 = nest_list[0][1]
print(val_2)

tuplex = ("tuple", False, 3.2, 1)
print(tuplex)

tuplex = (4, 6, 2, 8, 3, 1)
print(tuplex)

tuplex = tuplex + (9,)
print(tuplex)

tuple1 = (50, 10, 60, 70, 50)
print(tuple1.count(50))

tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1, 888, 888, 888, 888, 888, 888, 888)

_slice = tuplex[3:5]

print(_slice)

_slice = tuplex[::6]
print(_slice)