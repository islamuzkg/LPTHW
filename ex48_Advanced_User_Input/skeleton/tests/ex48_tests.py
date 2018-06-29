# Reference link: https://github.com/bitsai/book-exercises/blob/master/Learn%20Python%20the%20Hard%20Way/projects/ex48/tests/ex48_tests.py#L36

from nose.tools import *
from ex48 import lexicon

def test_directions():
	assert_equal(lexicon.scan("north"),[('direction', 'north')])
	result = lexicon.scan("north south east")
	assert_equal(result, [('direction', 'north'),
				('direction', 'south'),
				('direction', 'east')])

def test_verbs():
	assert_equal(lexicon.scan("go"), [('verb', 'go')])
	result = lexicon.scan("go kill eat open")
	assert_equal(result, [('verb', 'go'),
				('verb', 'kill'),
				('verb', 'eat'),
				('verb', 'open')])

def test_nouns():
	assert_equal(lexicon.scan("bear"), [('noun', 'bear')])
	result = lexicon.scan("bear princess")
	assert_equal(result, [('noun', 'bear'),
				('noun', 'princess')])

def test_numbers():
	assert_equal(lexicon.scan("1234"), [('number', 1234)])
	result = lexicon.scan("3 91234")
	assert_equal(result, [('number', 3),
				('number', 91234)])

def test_errors():
	assert_equal(lexicon.scan("ASDFADFASDF"), [('error', 'ASDFADFASDF')])
	result = lexicon.scan("bear I AS princess")
	assert_equal(result, [('noun', 'bear'),
				('error', 'IAS'),
				('noun', 'princess')])

def test_capitalization():
	result = lexicon.scan("the The tHe thE")
	assert_equal(result, [('stop', 'the'),
				('stop', 'the'),
				('stop', 'the'),
				('stop', 'the')])
