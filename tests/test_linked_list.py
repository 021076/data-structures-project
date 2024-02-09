"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src.linked_list import LinkedList, Node


class TestLinkedList(unittest.TestCase):
    def test_node(self):
        node = Node({'data0': 0})
        self.assertEqual(str(type(node)), "<class 'src.linked_list.Node'>")
        self.assertEqual(str(node), "{'data0': 0}")

    def test_llist(self):
        ll = LinkedList()
        self.assertEqual(str(type(ll)), "<class 'src.linked_list.LinkedList'>")

    def test_insert(self):
        ll = LinkedList()
        self.assertEqual(str(ll), "None")
        ll.insert_beginning({'id': 1})
        self.assertEqual(str(ll), "{'id': 1}-> None")
        ll.insert_beginning({'id': 0})
        self.assertEqual(str(ll), "{'id': 0}-> {'id': 1}-> None")
        ll.insert_at_end({'id': 2})
        self.assertEqual(str(ll), "{'id': 0}-> {'id': 1}-> {'id': 2}-> None")
        ll.insert_at_end({'id': 3})
        self.assertEqual(str(ll), "{'id': 0}-> {'id': 1}-> {'id': 2}-> {'id': 3}-> None")