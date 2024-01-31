"""Здесь надо написать тесты с использованием unittest для модуля queue."""

import unittest
from src.queue import Queue


class TestQueue(unittest.TestCase):
    def test_enqueue_queue(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        self.assertEqual(queue.head.data, 'data1')
        self.assertEqual(queue.tail.data, 'data2')

    def test_str_queue(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        self.assertEqual(str(queue), "data1\ndata2")
