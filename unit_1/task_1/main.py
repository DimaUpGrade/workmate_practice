from typing import Any

class ObjList:
    __next: 'ObjList | None' = None
    __prev: 'ObjList | None' = None
    __data = None
    
    def __init__(self, data: Any) -> None:
        self.set_data(data)

    def set_next(self, obj: 'ObjList') -> None:
        self.__next = obj

    def set_prev(self, obj: 'ObjList') -> None:
        self.__prev = obj

    def set_data(self, data: Any) -> None:
        self.__data = data

    def get_next(self) -> 'ObjList | None':
        return self.__next

    def get_prev(self) -> 'ObjList | None':
        return self.__prev

    def get_data(self) -> Any:
        return self.__data


class LinkedList:
    head: ObjList | None = None
    tail: ObjList | None = None

    def __init__(self) -> None:
        pass
    
    # add object in the end of linked list
    def add_obj(self, obj: ObjList | None) -> None:
        if self.head == None:
            self.head = obj
        else:
            self.tail.set_next(obj)
            obj.set_prev(self.tail)

        self.tail = obj

    # remove last element
    def remove_obj(self) -> None:
        if self.tail:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.get_prev()
                self.tail.set_next(None)

    # return list of all elements
    def get_data(self) -> list:
        data = list()
        if self.head:
            current = self.head
            data.append(current.get_data())

            while current.get_next():
                current = current.get_next()
                data.append(current.get_data())
            
        return data


# lst = LinkedList()
# lst.add_obj(ObjList("Данные 1"))
# lst.add_obj(ObjList("Данные 2"))
# lst.add_obj(ObjList("Данные 3"))
# lst.remove_obj()
# lst.add_obj(ObjList("Данные 4"))
# res = lst.get_data()
# print(res)
