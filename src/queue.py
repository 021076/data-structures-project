class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node
        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь
        :param data: данные, которые будут добавлены в очередь
        """
        new_node = Node(data, None)
        if self.tail is None and self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next_node = new_node
            self.tail = self.tail.next_node

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента
        :return: данные удаленного элемента
        """
        if self.head is None:
            return None
        else:
            removed = self.head.data
            self.head = self.head.next_node
            return removed

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        list_queue = ""
        queue = self.head
        while queue:
            list_queue += (str(queue.data) + "\n")
            queue = queue.next_node
        list_queue = list_queue.strip("\n")
        if len(list_queue):
            return list_queue
        else:
            return ""

    # Рекомендация наставника:
    # немного сложно сделала - можно закидывать элементы в список и потом его возвращать,
    # преобразовывая к строке, пока существует следующая нода
    # def __str__(self) -> str:
    #     queue_items = []
    #     head_node: Node = self.head
    #     while head_node:
    #         queue_items.append(str(head_node.data))
    #         head_node = head_node.next_node
    #     return '\n'.join(queue_items)
