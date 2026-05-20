from My_List import MyList

if __name__ == "__main__":
    my_list = MyList()

    my_list.addFirst(3)
    my_list.addLast(2)
    my_list.addLast(5)
    my_list.addLast(2)
    my_list.addLast(7)
    my_list.addLast(6)
    my_list.traverse()

    my_list.sort_from_to(2, 4)
    my_list.traverse()