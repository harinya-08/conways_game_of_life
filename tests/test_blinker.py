# tests/test_blinker.py
import pytest
from game import next_gen

def test_blinker_oscillator():
    blinker = {(1,0), (1,1), (1,2)}
    next_blink = next_gen(blinker)
    expected = {(0,1), (1,1), (2,1)}
    assert next_blink == expected
