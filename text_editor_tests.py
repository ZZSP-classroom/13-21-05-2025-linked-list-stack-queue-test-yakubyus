import unittest
from text_editor_2 import Stack

class TestStack(unittest.TestCase):
    def test_push_pop(self):
        stack = Stack()
        
        stack.push("Typed: Hello")
        stack.push("Typed: World")
        
        self.assertEqual(stack.peek(), "Typed: World")

        stack.pop()
        self.assertEqual(stack.peek(), "Typed: Hello")
        
    def test_empty_stack(self):
        stack = Stack()
        
        self.assertIsNone(stack.pop())

        self.assertIsNone(stack.peek())
        
    def test_size(self):
        stack = Stack()
        
        stack.push("Typed: Hello")
        stack.push("Typed: World")

        self.assertEqual(len(stack.stack), 2)
        
        stack.pop()
        self.assertEqual(len(stack.stack), 1)

if __name__ == '__main__':
    unittest.main()
