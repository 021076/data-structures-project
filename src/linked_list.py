class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, node):
        self.node = node
        self.next = None  # указатель на следующий узел

    def __str__(self):
        return str(self.node)


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.head = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = None
            return None
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
        last_node.next = new_node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)
        ll_string = ""
        while node:
            ll_string += f'{str(node.node)}-> '
            node = node.next
        ll_string += 'None'
        return ll_string

    def to_list(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def get_data_by_id(self, key):
        node = self.head
        while node:
            if node == key:
                return True
            else:
                node = node.next
        return False
