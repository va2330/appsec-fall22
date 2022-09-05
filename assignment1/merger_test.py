from merger import Mergesort
import argparse
import pytest
import sys

class TestMergesort():
    merger = Mergesort()
    
    def test_merger_sorted_arrays(self):
        self.merger.clean()
        a = [1,3,5]
        b = [2,4,6]
        self.merger.set_left(a)
        self.merger.set_right(b)
        res = [1,2,3,4,5,6]
        assert self.merger.sort() == res

    # def test_merger_unsorted_arrays(self):
    #     self.merger.clean()
    #     a = [1,5,3]
    #     b = [2,4,6]
    #     self.merger.set_left(a)
    #     self.merger.set_right(b)
    #     res = [1,2,3,4,5,6]
    #     assert self.merger.sort() == res


