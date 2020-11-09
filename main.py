
list_to_sort = [[3, 3, 4], [2, 1, 1], [3, 2, 2]]

suma = 0
i= 0
while i < 2:
    if list_to_sort[0][2]==list_to_sort[++i][2]:
        suma+=1
    i+=1
    if suma>1:
        list_to_sort.sort(key=lambda list_element: list_element[2],reverse=False)
    else:
        list_to_sort.sort(key=lambda list_element: list_element[1],reverse=False)

print(list_to_sort)