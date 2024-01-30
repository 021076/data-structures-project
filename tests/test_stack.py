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
        removed = stack.pop()
        self.assertEqual(stack.top.data, 'data1')
        self.assertEqual(removed, 'data2')
