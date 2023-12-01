class Node:
    """Класс для узла очереди"""

    def __init__(self, data):  # ---next_node????
        """
        Конструктор класса Node
        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = None


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
        if self.tail is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next_node = Node(data)
            self.tail = self.tail.next_node

    def __str__(self):
        #     """Магический метод для строкового представления объекта"""
        list_queue = ""
        queue = self.head
        while queue:
            list_queue += (str(queue.data) + ", ")
            # list_queue += (str(queue.data) + "\\n")
            queue = queue.next_node
        list_queue = list_queue.strip(", ")
        # list_queue = list_queue.strip("\\n")
        if len(list_queue):
            return list_queue
        else:
            return ""
