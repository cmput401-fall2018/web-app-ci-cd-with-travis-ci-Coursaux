from service import *
from unittest.mock import patch

@patch('service.Service.bad_random', return_value = 1)
def test_bad_random(bad_random):
	s = Service()
    assert s.bad_random() == 1

@patch('service.Service.bad_random', return_value = 10)
def test_divide(bad_random):
	s = Service()
    assert s.divide(-5) == -2
    assert s.divide(10) == 1
	assert s.divide(1) == 10
	assert s.divide(4) == 2.5
	
def test_abs_plus():
	s = Service()
	assert s.abs_plus(1) == 2
	assert s.abs_plus(-1) == 2
	assert s.abs_plus(0) == 1
    assert s.abs_plus(10.1) == 11.1

@patch('service.Service.bad_random', return_value = 10)
def test_complicated_function(bad_random):
	s = Service()
	assert s.complicated_function(10) == (1, 0)
	assert s.complicated_function(4) == (2.5, 0)
	assert s.complicated_function(-1) == (-10, 0)
    assert s.complicated_function(0.5) == (20, 0)

test_divide()
test_abs_plus()
test_complicated_function()
test_bad_random()
