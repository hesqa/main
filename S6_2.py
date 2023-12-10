def remove_element_from_tuple(my_tup, e):
    if e in my_tup:
        index = my_tup.index(e)
        new_tup = my_tup[:index] + my_tup[index + 1:]
        return new_tup
    else:
        return my_tup

t1 = (1, 2, 3)
r1 = remove_element_from_tuple(t1, 1)
print(r1)

t2 = (1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2)
r2 = remove_element_from_tuple(t2, 3)
print(r2)

t3 = (2, 4, 6, 6, 4, 2)
r3 = remove_element_from_tuple(t3, 9)
print(r3)
