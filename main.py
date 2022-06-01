from linked_list import Queue


def main():
    my_list = Queue()
    my_list.addelement(3, 3)
    my_list.addelement(10, 3)
    my_list.addelement(3, 3)
    my_list.addelement(3, 3)
    my_list.addelement(3, 58)
    my_list.addelement(6, 3)
    print("My list:")
    print(my_list)
    print("Deleted element:")
    print(my_list.delete_element())
    print("My list:")
    print(my_list)
    print("Search results: ")
    print(my_list.search(3, 3))
    print("Distance between two points")
    print(my_list.distance_between_first_and_last())
    print("Length of the list")
    print(my_list.get_length())


if __name__ == '__main__':
    main()

