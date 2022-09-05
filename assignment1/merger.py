#!/usr/bin/env python3

class Mergesort:
    """
    A class that uses merge sort algorithm to merge two arrays
    """
    def __init__(self,left = None, right = None):
        if left is not None:
            self.left = left
        if right is not None:
            self.right = right
        self.res = None
    
    def set_left(self, left):
        """
        sets left array
        """
        self.left = left
    
    def set_right(self, right):
        """
        sets right array
        """
        self.right = right

    def merge(self):
        """
        merges two arrays
        """
        self.res = []
        l = len(self.left) + len(self.right)
        while l > 0:
            first = self.left[0] if len(self.left) > 0 else 1000000
            second = self.right[0] if len(self.right) > 0 else 1000000
            if first < second:
                self.res.append(self.left.pop(0))
            else:
                self.res.append(self.right.pop(0))
            l -= 1

    def sort(self):
        """
        returns the sorted result
        """
        if self.res is None:
            self.merge()
        return self.res
    
    def clean(self):
        """
        resetting the variables
        """
        self.left = None
        self.right = None
        self.res = None



if __name__ == "__main__":
    a = [1,3,5]
    b = [2,4,6]
    m = Mergesort(a,b)
    print(a)
    print(b)
    print(m.sort())
