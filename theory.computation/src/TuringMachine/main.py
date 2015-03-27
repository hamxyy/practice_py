'''
Created on 26 Mar, 2015

@author: z0037v8z
'''
from src.TuringMachine.TuringMachine import TuringMachineTransition, TuringMachine, TuringMachineState
from src.TuringMachine.Constant import MoveDirection
import re

def transit(curState, nextChar, transitions):
    result = transitions[curState.name][nextChar]
    return TuringMachineTransition(result[0], result[1], result[2])

def makeTuringMachine(spec):
    simpleTranRe = r"(?P<state>\w+),(?P<input>[\w|\s])\-\>(?P<next>\w+),(?P<dir>[L|R])"
    writeTransRe = r"(?P<state>\w+),(?P<input>[\w|\s])\-\>(?P<next>\w+),(?P<write>[\w|\s]),(?P<dir>[L|R])"
    states = []
    acceptState = None
    rejectState = None
    transitions = {}
    for line in spec.splitlines():
        if(not line or line == ""):
            continue 
        if(re.match(simpleTranRe, line)):
            result = re.match(simpleTranRe, line)
            state = TuringMachineState(result.group("state"))
            nextState = TuringMachineState(result.group("next"))
            nextChar = result.group("input")
            direction = MoveDirection.LEFT if result.group("dir") == "L" else MoveDirection.RIGHT
            writeChar = ''
        elif(re.match(writeTransRe, line)):
            result = re.match(writeTransRe, line)
            state = TuringMachineState(result.group("state"))
            nextState = TuringMachineState(result.group("next"))
            nextChar = result.group("input")
            direction = MoveDirection.LEFT if result.group("dir") == "L" else MoveDirection.RIGHT
            writeChar = result.group("write")
        else:
            raise
        states.append(state)
        stateName = state.name
        if(stateName not in transitions): 
            transitions[stateName] = {}
        if(stateName == "q_accept"):
            acceptState = state        
        if(stateName == "q_reject"):
            rejectState = state
        transitions[stateName][nextChar] = [nextState, writeChar, direction]
    acceptState = acceptState if acceptState else TuringMachineState("q_accept")
    rejectState = rejectState if rejectState else TuringMachineState("q_reject")
    transitionFunction = lambda curState, nextChar: transit(curState, nextChar, transitions)
    return TuringMachine(states, transitionFunction, states[0], acceptState, rejectState)

tmspec = open("sampletm").read()
tm = makeTuringMachine(tmspec)
print(tm.run("0000"))