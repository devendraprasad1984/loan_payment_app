# from abc import ABC, abstractmethod

class ProcessHandler():
    """common data handling logic"""

    def handle(self, data=None, type=None):
        """handle derived classes handler logic"""
        print(f'data handle from child {type} - {data}')
