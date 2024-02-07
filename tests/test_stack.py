"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Node, Stack


class TestStack(unittest.TestCase):
    def test_node(self):
        self.assertEqual((Node(5, None)).data, 5)
        self.assertEqual((Node('a', 5)).data, 'a')

    def test_push_stack(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        self.assertEqual(stack.top.data, 'data2')
        self.assertEqual(stack.top.next_node.data, 'data1')

    def test_pop_stack(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        removed1 = stack.pop()
        self.assertEqual(stack.top.data, 'data1')
        self.assertEqual(removed1, 'data2')
        removed2 = stack.pop()
        self.assertEqual(stack.top, None)
        self.assertEqual(removed2, 'data1')

    def test_str_stack(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        self.assertEqual(str(stack), "[data2, data1]")
        stack.pop()
        stack.pop()
        self.assertEqual(str(stack), "[]")
