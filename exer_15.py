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

    @property
    def duration(self):
        return f"Playlist: '{self.name}' -- {len(self.songs)} songs"
    
    def __len__(self):
        return len(self.songs)
    
    def __contains__(self, item):
        for song in self.songs:
            if song == item:
                return True
        return False

    def __iter__(self):
        self._index = 0
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
        if not isinstance(other, Playlist):
            raise NotImplementedError("unsupported operand for +")
        cls = Playlist(self.name +" and "+ other.name)
        cls.songs = self.songs + other.songs
        return cls


tracks = Playlist("worship songs")
tracks.add("to know you", "Haske")
print(tracks.songs)
tags = Playlist("praise songs")
tags.add("Awesome God","my Daddy")
print(tags.songs)

# it = iter(tracks)
# print(next(it))
# print(next(it))

for i in tracks:
    print(i)

new = tags + tracks

print(new.songs)

print(tracks.duration)