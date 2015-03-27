'''
Created on 25 Mar, 2015

@author: z0037v8z
'''
from src.TuringMachine.Constant import MoveDirection, Result, Seperator

class TuringMachine(object):

    def __init__(self, states, transitionFunction, startState, acceptState, rejectState, inputAlphabet=[], tapeAlphabet=[]):
        self.states = states
        self.inputAlphabet = inputAlphabet
        self.tapeAlphabet = tapeAlphabet
        self.transitionFunction = transitionFunction
        self.curState = startState
        self.acceptState = acceptState
        self.rejectState = rejectState
    
    def _log(self):
        print(self.curState.name + ":" + self.tape.toString())
    
    def run(self, inputStr):
        self.pos = 0
        self.tape = TuringMachineTape(inputStr)
        while(True):
            self._log()
            if(self.curState.equals(self.acceptState)):
                return Result.ACCEPT
            if(self.curState.equals(self.rejectState)):
                return Result.REJECT
            trans = self.transitionFunction(self.curState, self.tape.read())
            self.curState = trans.nextState
            self.tape.write(trans.writeChar)
            self.tape.move(trans.moveDirection)

class TuringMachineState(object):
    def __init__(self, name):
        self.name = name
        
    def equals(self, another):
        return self.name == another.name

    def __repr__(self):
        return self.name
    

class TuringMachineTape(object):
    def __init__(self, content):
        self.content = content
        self.pos = 0
    
    def move(self, direction):
        if(direction == MoveDirection.RIGHT):
            self.pos += 1
            if(len(self.content) <= self.pos):
                self.content = self.content + " "
        elif(direction == MoveDirection.LEFT):
            self.pos -= 1
            if(self.pos < 0):
                self.pos = 0
    
    def read(self):
        return self.content[self.pos]
    
    def write(self, c):
        if(c == ""):
            return
        s = list(self.content)
        s[self.pos] = c
        self.content = "".join(s)
        
    def toString(self):
        return self.content[0:self.pos] + Seperator.BAR + self.content[self.pos:len(self.content)]

class TuringMachineTransition(object):
    def __init__(self, nextState, writeChar, moveDirection):
        self.nextState = nextState
        self.writeChar = writeChar
        self.moveDirection = moveDirection
