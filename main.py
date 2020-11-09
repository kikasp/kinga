

list_to_sort_2 = [[3, 2, 3], [2, 0, 2], [3, 0, 1], [3, 1, 0]]


list_to_sort = [[3, 2, 3], [2, 4, 2], [3, 0, 1]]

i= 0
while i < 3:
    list_to_sort[i][2]==list_to_sort[++i][2]
    i+=1
    list_to_sort.sort(key=lambda list_element:list_element[2])
else:
    list_to_sort.sort(key=lambda list_element: list_element[1])

print(list_to_sort)