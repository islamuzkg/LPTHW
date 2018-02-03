class Song(object):
	
	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["Happy birthday to you",
				  "I don't want to get sued",
				  "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
						"Which pockets full of shells",
						'^' * 30])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

my_song = Song(["\n",
				"Head and shoulders",
				"Knees and toes",
				"Knees and toes"])
a = '*' * 30
my_song1 = Song([a,
				 "And eyes and ears",
				 "And mouth",
				 "And nose"])

my_song.sing_me_a_song()
my_song1.sing_me_a_song()
my_song.sing_me_a_song()

twinkle = Song(["Twinkle, twinle little start,",
				"time to clean up where you are.",
				"Put the toys back in their place.",
				"Keep a smile  upon your face.",
				"Twinle, twinle little start,",
				"time to clean up where you are."])
print '_' * 30
twinkle.sing_me_a_song()

