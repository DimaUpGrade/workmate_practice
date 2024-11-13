from typing import TypeVar, Self

T = TypeVar("T")


class ObjList:
    """
    This class realizes logic of linked list's objects
    """
    __next: Self | None = None
    __prev: Self | None = None
    __data = None
    
    def __init__(self, data: TypeVar) -> None:
        """
        Initialize of list's object
        """
        self.set_data(data)

    def set_next(self, obj: Self) -> None:
        """
        Set next element's link in the list
        """
        self.__next = obj

    def set_prev(self, obj: Self) -> None:
        """
        Set previous element's link in the list
        """
        self.__prev = obj

    def set_data(self, data: T) -> None:
        """
        Set data of list's element
        """
        self.__data = data

    def get_next(self) -> Self | None:
        """
        Get next element's link in the list
        """
        return self.__next

    def get_prev(self) -> Self | None:
        """
        Get previous element's link in the list
        """
        return self.__prev

    def get_data(self) -> T:
        """
        Set data of list's element
        """
        return self.__data


class LinkedList:
    """
    This class realizes linked list logic
    and works with ObjList class
    """
    head: ObjList | None = None
    tail: ObjList | None = None

    def add_obj(self, obj: ObjList | None) -> None:
        """
        Add object in the end of linked list
        """
        if self.head is None:
            self.head = obj
        else:
            self.tail.set_next(obj)
            obj.set_prev(self.tail)

        self.tail = obj

    def remove_obj(self) -> None:
        """
        Remove last element from the linked list
        """
        if self.tail:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.get_prev()
                self.tail.set_next(None)

    def get_data(self) -> list:
        """
        Return list of all elements
        """
        data = list()
        if self.head:
            current = self.head
            data.append(current.get_data())

            while current.get_next():
                current = current.get_next()
                data.append(current.get_data())
            
        return data
