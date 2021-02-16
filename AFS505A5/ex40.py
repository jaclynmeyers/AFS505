

class Song(object):
    def _init_(self, lyrics):
    self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
"I don't want to get sued",
"So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
"With pockets full of shells"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()

class Song(object):
    def _init_(self, lyrics):
    self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

chsristmas_song = Song(["We wish you a Merry Christmas",
"And a happy New Year",
"So I'll stop right there"])

hokie_pokie = Song(["They do the hokie pokie", "and they turn themselves around"])

christmas_song.sing_me_a_song()
hokie_pokie.sing_me_a_song()

hokie_pokie = ({"They do the hokie pokie", "and they turn themselves around"})

mystuff['apples']
mystuff.apples()
print(mystuff.tangerine)

things = MyStuff()
thing.apples()
print(thing.tangerine)
