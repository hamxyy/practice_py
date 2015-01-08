'''
Created on 16 Dec, 2014

@author: z0037v8z
'''
import re

TAG_NUMBER = 256
TAG_ID = 257

class SyntaxTreeNode():
    def __init__(self, value):
        self.children = []
        self.value = value

class AbstractSyntaxTree(SyntaxTreeNode):
    def __init__(self, root):
        self.root = root

class Token():
    def __init__(self, tag):
        self.tag = tag

    def __str__(self):
        return str(self.tag)
    
class Number(Token):
    def __init__(self, value):
        self.tag = TAG_NUMBER
        self.value = value
    
    def __str__(self):
        return str(self.value)

class Word(Token):
    def __init__(self, lexeme):
        self.tag = TAG_ID
        self.lexeme = lexeme
        
    def __str__(self):
        return self.lexeme

class LexicalAnalyzer():
    ignored = [' ', '\n', '\t']
    words = {"int" : Word("int")}
    operators = ['+', '-', '*', '/', '=']

    def process(self, source):
        self.source = source + "\0"
        self.pos = 0
    
    def scan(self):
        peek = self.current()
        while(True):
            if(peek in self.ignored):
                peek = self.read()
                continue
            if(re.match(r"\d", peek)):
                v = 0
                while(re.match(r"\d", peek)):
                    v = 10 * v + int(peek)
                    peek = self.read()
                return Number(v)
            if(re.match(r"[\w_]", peek)):
                s = ""
                while(re.match(r"[\w_]", peek)):
                    s += peek
                    peek = self.read()
                word = self.words.get(s)
                if(not word):
                    word = Word(s)
                    self.words[s] = word
                return word
            t = Token(peek)
            self.read()
            return t
    
    def current(self):
        return self.source[self.pos]
    
    def read(self):
        self.pos += 1
        return self.source[self.pos]

def parse(source):
    print("Parsing \"" + source + "\"...")
    root = SyntaxTreeNode('root')
    if(match_exp(source, root)):
        print(calculate(root.children[0]))
        return True
    else:
        return False

def match_number(c, node):
    match = re.match(r"\d+", c)
    if(match):
        node.children.append(SyntaxTreeNode(c))
        return True
    else:
        return False

def match_exp(e, node):
    return match_plus(e, node)     \
        or match_minus(e, node)    \
        or match_multiply(e, node) \
        or match_divide(e, node)   \
        or match_number(e, node)   \
        
def match_operator(op, e, node):
    match = re.match(r"^(.*)" + "\\" + op + r"(\d)$", e)
    if(match):
        plus_node = SyntaxTreeNode(op)
        node.children.append(plus_node)
        right_operand_node = SyntaxTreeNode(match.group(2))
        match_exp_result = match_exp(match.group(1), plus_node)
        plus_node.children.append(right_operand_node)
        if(match_exp_result):
            return True
    return False

def match_plus(e, node):
    return match_operator("+", e, node)
    
def match_minus(e, node):
    return match_operator('-', e, node)

def match_multiply(e, node):
    return match_operator("*", e, node)
    
def match_divide(e, node):
    return match_operator('/', e, node)

def calculate(node):
    if(node.value == "+"):
        return calculate(node.children[0]) + calculate(node.children[1])
    elif(node.value == "-"):
        return calculate(node.children[0]) - calculate(node.children[1])
    else:
        return int(node.value)
