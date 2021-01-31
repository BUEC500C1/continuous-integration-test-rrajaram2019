from UnitConverter import *
import pytest

def test_distance():
  assert myParser("1 foot to inches") == "12.0 inches"

def test_weight():
  assert myParser("convert 1 kg into ounces") == "35.3 ounces"

def test_temperature():
  assert myParser("what's 1 celcius in fahrenheit?") == "33.8 fahrenheit"

