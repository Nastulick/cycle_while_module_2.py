my_list=[42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
zero = 0
while True:
    if my_list[zero] > 0 :
        print(my_list[zero])
        zero += 1
    elif my_list[zero] < 0 :
        break
    else:
        zero += 1
