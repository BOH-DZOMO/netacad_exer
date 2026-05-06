class Playlist():
    def __init__(self,name):
        self.name  = name
        self.songs = []
        self._stop = 0
        self._index = 0
        self._next = 1

    def add(self,*items):
        if len(items) == 0: return
        for i in items:
            self.songs.append(i)
    
    def __len__(self):
        return len(self.songs)
    
    def __contains__(self, item):
        for song in self.songs:
            if song == item:
                return True
        return False

    def __iter__(self):
        return self
    
    def __next__(self):
        self._stop = len(self.songs)
        if self._index < self._stop:
            self._index += 1
            return self.songs[self._index - 1]
        else:
            raise StopIteration
    
    def __getitem__(self, key):
        return self.songs[key]
        
    def __add__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError(
                "unsupported operand for +"
            )
        cls = Playlist(self.name + other.name)
        cls.add(*self.songs)
        cls.add(*other.name)
        return cls


tracks = Playlist("worship songs")
tracks.add("to know you", "Haske")
print(tracks.songs)

# it = iter(tracks)
# print(next(it))
# print(next(it))

for i in tracks:
    print(i)