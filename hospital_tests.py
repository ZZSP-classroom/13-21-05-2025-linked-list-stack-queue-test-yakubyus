import unittest
from hospital_1 import Patient, Queue

class TestQueue(unittest.TestCase):
    def test_enqueue_dequeue(self):
        queue = Queue()
        patient1 = Patient("Alice", "10:00 AM")
        patient2 = Patient("Bob", "10:30 AM")
        
        queue.enqueue(patient1)
        queue.enqueue(patient2)
        
        self.assertEqual(queue.peek().name, "Alice")

        queue.dequeue()
        self.assertEqual(queue.peek().name, "Bob")
        
    def test_empty_queue(self):
        queue = Queue()

        self.assertIsNone(queue.dequeue())
        
        self.assertIsNone(queue.peek())
        
    def test_size(self):
        queue = Queue()
        patient1 = Patient("Alice", "10:00 AM")
        patient2 = Patient("Bob", "10:30 AM")
        
        queue.enqueue(patient1)
        queue.enqueue(patient2)
        
        self.assertEqual(queue.size(), 2)
        
        queue.dequeue()
        self.assertEqual(queue.size(), 1)

if __name__ == '__main__':
    unittest.main()
