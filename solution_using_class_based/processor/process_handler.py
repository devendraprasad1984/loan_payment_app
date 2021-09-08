# from abc import ABC, abstractmethod

class ProcessHandler():
    """common data handling logic"""


    def handle(self, type=None, **kwargs):
        """handle derived classes handler logic"""
        print(f'data handle from child {type} - {kwargs}')
