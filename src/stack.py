class Node:
    """Класс для узла стека"""

    def __init__(self, data):
        """
        Конструктор класса Node
        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = None


# если init так, то не будет работать n2 = Node('a', n1)
# если в аргументы init добавить next_node и инициализировать: self.next_node = next_node, тогда push не работает

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
            self.top = Node(data)
        else:
            new_node = Node(data)
            new_node.next_node = self.top
            self.top = new_node
