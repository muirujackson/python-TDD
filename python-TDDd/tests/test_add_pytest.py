#!/usr/bin/python3

import pytest
import sys

#setting the path
sys.path.append('.')


from my_module import add

class TestAdd:
    def test_2_and_2(self):
        assert add(2, 2) == 4

    def test_negative_number(self):
        assert add(-2, -2) == -4

    def test_float_and_int(self):
        assert add(2.5, 3) == 5

    def test_str_and_int(self):
        with pytest.raises(TypeError):
            add(2, "3")

