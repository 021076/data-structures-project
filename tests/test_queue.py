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
        queue.dequeue()
        queue.dequeue()
        self.assertEqual(str(queue), "")

    def test_dequeue_queue(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        removed1 = queue.dequeue()
        self.assertEqual(queue.head.data, 'data2')
        self.assertEqual(removed1, 'data1')
        removed2 = queue.dequeue()
        self.assertEqual(queue.head, None)
        self.assertEqual(removed2, 'data2')
