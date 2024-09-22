#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name='', job=''):
        self.name = name  # This will use the setter for validation
        self.job = job    # This will use the setter for validation
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0 or len(value) > 25:
            print("Name must be string between 1 and 25 characters.")
            self._name = None  # Ensure _name is set to None if invalid
        else:
            self._name = value.title()
    
    @property
    def job(self):
        return self._job
    
    @job.setter
    def job(self, value):
        if value not in APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
            self._job = None  # Ensure _job is set to None if invalid
        else:
            self._job = value
