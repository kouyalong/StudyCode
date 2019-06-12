#!/usr/bin/env python3
# coding: utf-8

from functools import partial


class Stack:
    """使用List实现栈的基本功能"""
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


def my_par_checker(simpleString):
    end_sym = [")", "]", "}"]
    start_sym = ["(", "[", "{"]
    match = lambda x, y: end_sym.index(x) == start_sym.index(y)
    stack = Stack()
    for s in simpleString:
        if s in end_sym:
            if stack.isEmpty():
                return False
            if match(s, stack.peek()):
                stack.pop()
            else:
                return False
        elif s in start_sym:
            stack.push(s)
    if stack.isEmpty():
        return True
    else:
        return False


def base_converter(dec_number, base):
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while dec_number > 0:
        rem = dec_number % base
        remstack.push(rem)
        dec_number = dec_number // base

    new_string = ""
    while not remstack.isEmpty():
        new_string += digits[remstack.pop()]
    return new_string


bin_converter = partial(base_converter, base=2)
dec_converter = partial(base_converter, base=8)
hex_converter = partial(base_converter, base=16)


def do_math(a, b, symbol):
    a, b = int(a), int(b)
    if symbol == "+":
        return a + b
    elif symbol == "-":
        return a - b
    elif symbol == "/":
        return a / b
    elif symbol == "*":
        return a * b


def postfix_evaluate(postfix_string):
    """后缀表达式求值"""
    post_list = postfix_string.split()
    symbols = ["+", "-", "*", "/"]
    stack = Stack()
    for p in post_list:
        if p in symbols:
            b = stack.pop()
            a = stack.pop()
            stack.push(do_math(a, b, p))
        else:
            stack.push(p)
    return stack.pop()


def prefix_evaluate(prefix_string):
    """前缀表达式求值"""
    post_list = prefix_string.split()
    symbols = ["+", "-", "*", "/"]
    stack = Stack()
    for p in post_list:
        if p in symbols or stack.peek() in symbols:
            stack.push(p)
        else:
            while not stack.isEmpty() and stack.peek() not in symbols:
                a = stack.pop()
                op = stack.pop()
                p = do_math(a, p, op)
            stack.push(p)
    return stack.pop()


def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)


class MyQueue(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def hot_kill(names, num):
    print(names)
    simqueue = MyQueue()
    for name in names:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        n = simqueue.dequeue()
        print(n)

    return simqueue.dequeue()


def convert_int(n, base):
    convert_string = "0123456789ABCDEF"
    if n < base:
        return convert_string[n]
    else:
        return convert_int(n//base, base) + convert_string[n % base]


bin_converter_2 = partial(convert_int, base=2)
dec_converter_2 = partial(convert_int, base=8)
hex_converter_2 = partial(convert_int, base=16)


class HashTable(object):

    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hash_function(self, key, size):
        return key % size

    def rehash(self, old_hash, size):
        return (old_hash + 1) % size

    def put(self, key, value):
        hash_value = self.hash_function(key, len(self.slots))
        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = value
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = value
            else:
                next_slot = self.rehash(hash_value, len(self.slots))
                while self.slots[next_slot] is not None and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot, len(self.slots))
                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = value
                else:
                    self.data[next_slot] = value

    def get(self, key):
        start_slot = self.hash_function(key, len(self.slots))
        data, position = None, start_slot
        stop, found = False, False
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)


ht = HashTable(10)
ht[23] = "cat"
ht[14] = "dog"
ht[51] = "bird"
ht[93] = "lion"
ht[20] = "chicken"
ht[55] = "pig"
ht[33] = "tiger"
print(ht.slots)
print(ht.data)
print(ht[99])


