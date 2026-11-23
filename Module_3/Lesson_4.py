my_set = {1, 2, 3, 3, 4, 5, 5, 5}
my_set = {1.0, "Hello", (1, 2, 3)}
my_set = {1, 2, 3, 4, 3, 2}
my_set = set([1, 2, 3, 2])
num_set = set([0, 1, 3, 4, 5])

print(num_set)
num_set.pop()
print("After removing the first element from the said set: ")
print(num_set,"\n")
print("=====")
num_list = [0, 1, 3, 4, 5]
print(num_list)
num_list.pop()
print("After removing the first element from the said set: ")
print(num_list,"\n")

setx = {"green", "blue"}
sety = {"blue", "yellow"}
print("Original set elements:")
print(setx)
print(sety)
print("\nIntersection of two said sets:")
setz = setx.intersection(sety)
print(setz)