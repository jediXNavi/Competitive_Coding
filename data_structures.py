#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 15:07:12 2021

@author: jedixnavi
"""


class Stack:
    def __init__(self):
        self.arr = []

    def isEmpty(self):
        return self.arr == []

    def push(self, item):
        self.arr.append(item)

    def pop(self):
        return self.arr.pop()

    def size(self):
        return len(self.arr)

    def peek(self):
        return self.arr[len(self.arr) - 1]


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        return self.queue.pop()

    def isEmpty(self):
        return self.queue == []

    def size(self):
        return len(self.queue)


class Deque:
    def __init__(self):
        self.deque = []

    def addFront(self, item):
        self.deque.append(item)

    def addRear(self, item):
        self.deque.insert(0, item)

    def removeFront(self):
        return self.deque.pop()

    def removeRear(self):
        return self.deque.pop(0)

    def isEmpty(self):
        return self.deque == []

    def size(self):
        return len(self.deque)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, new_data):
        self.data = new_data

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext)


class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.left_child = None
        self.right_child = None

    def add_left(self, newNode):
        if self.left_child is None:
            self.left_child = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.left_child = self.left_child
            self.left_child = t

    def add_right(self, newNode):
        if self.right_child is None:
            self.right_child = newNode
        else:
            t = BinaryTree(newNode)
            t.right_child = self.right_child
            self.right_child = t

    def get_right(self):
        return self.right_child

    def get_left(self):
        return self.left_child

    def get_root_val(self):
        return self.key

    def set_root_val(self, new_root):
        self.key = new_root
