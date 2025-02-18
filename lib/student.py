#!/usr/bin/env python

from lib.user import User  # Ensure correct import

class Student(User):  # Inherit from User
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)  # Correct inheritance
        self.knowledge = []  # Initialize empty knowledge list

    def learn(self, new_knowledge):
        self.knowledge.append(new_knowledge)  # Add new knowledge
