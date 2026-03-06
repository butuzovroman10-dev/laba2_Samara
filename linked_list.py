class Node:
    """Узел односвязного списка"""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Односвязный список"""
    def __init__(self):
        self.head = None

    def append(self, data):
        """Добавление элемента в конец списка"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        """Вывод списка в консоль"""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def to_list(self):
        """Преобразование списка в обычный список Python (для удобного вывода)"""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result