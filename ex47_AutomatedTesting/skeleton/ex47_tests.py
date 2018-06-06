from nose.tools import *
import ex47 import Room

def test_room():
	gold = Room("GoldRoom",
			"""This room has gold in it you can grab. There's a door to the north.""")
	assert_equal(gold.name, "GoldRoom")
	assert_equal(gold.paths, {})

def test_room_paths():
	center = Room("Center", "Test room in the center.")
	north = Room("North", "Test room in the north.")
	south = Room("South", "Test room in the south.")

	center.add_path({'north': north, 'south': south})

def test_map():
	start = Room("Start", "You can go west and down a hole.")
	west = Room("Trees", "There are trees here, you can go east.")
	down = Room("Dongeon", "It is dark down here, you can go up")

	assert_equal(start.go('west'), west)
	assert_equal(start.go('east'), start)
	assert_equal(start.go('down'), start)
