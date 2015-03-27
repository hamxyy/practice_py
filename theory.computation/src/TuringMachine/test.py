'''
Created on 27 Mar, 2015

@author: z0037v8z
'''
import unittest
from src.TuringMachine.TuringMachine import TuringMachineTape
from src.TuringMachine.Constant import MoveDirection


class Test(unittest.TestCase):

    def setUp(self):
        self.tape = TuringMachineTape("abcde")

    def test_tape_runs(self):
        self.assertEqual(self.tape.read(), 'a')
        self.tape.move(MoveDirection.RIGHT)
        self.assertEqual(self.tape.read(), 'b')
        
    def test_tape_when_move_left_and_already_leftmost_then_stay(self):
        self.tape.move(MoveDirection.LEFT)
        self.assertEqual(self.tape.read(), 'a')

    def test_tape_when_move_right_and_already_rightmost_then_add_space(self):
        self.tape.move(MoveDirection.RIGHT)
        self.tape.move(MoveDirection.RIGHT)
        self.tape.move(MoveDirection.RIGHT)
        self.tape.move(MoveDirection.RIGHT)
        self.assertEqual(self.tape.read(), 'e')
        self.tape.move(MoveDirection.RIGHT)
        self.assertEqual(self.tape.read(), ' ')

    def test_tape_when_write_char_then_write(self):
        self.tape.write('x')
        self.assertEqual(self.tape.read(), 'x')

    def test_tape_when_write_empty_char_then_do_nothing(self):
        self.tape.write('')
        self.assertEqual(self.tape.read(), 'a')
        

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
