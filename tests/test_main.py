import os, io, json, math, re, importlib
import pytest
mod = importlib.import_module('main')


def test_fizzbuzz():
    out = mod.fizzbuzz(16)
    assert out[:5] == ["1","2","fizz","4","buzz"]
    assert out[14] == "fizzbuzz"
    assert len(out) == 16
