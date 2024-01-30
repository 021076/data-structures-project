class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node
        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека
        :param data: данные, которые будут добавлены на вершину стека
        """
        if self.top is None:
            self.next_node = None
            self.top = Node(data, None)
        else:
            self.next_node = self.top
            new_node = Node(data, self.next_node)
            new_node.next_node = self.top
            self.top = new_node
        # Или рекомендация наставника: упростить метод
        # self.top = Node(data, self.top)

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения
        :return: данные удаленного элемента
        """
        if self.top is None:
            return None
        elif self.top.next_node is None:
            removed = self.top.data
            self.top = None
            return removed
        else:
            removed = self.top.data
            self.top = self.top.next_node
            return removed

    def __str__(self):
        list_stack = ""
        stack = self.top
        while stack:
            list_stack += (str(stack.data) + ", ")
            stack = stack.next_node
        list_stack = list_stack.strip(", ")
        if len(list_stack):
            return f"[{list_stack}]"
        else:
            return "[]"
