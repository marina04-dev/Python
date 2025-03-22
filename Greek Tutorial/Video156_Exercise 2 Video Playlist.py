from random import randrange, seed
from datetime import datetime

class Video:
    def __init__(self, artist, title, duration):
        self.artist = artist
        self.title = title
        self.duration = duration
        
    def __str__(self):
        return f"{self.artist} - {self.title} ({self.duration})"
        
    
    
class Playlist:
    def __init__(self, title, descr, duration, videos):
        self.title = title
        self.descr = descr
        self.duration = duration
        self.videos = videos
        
    def __str__(self):
        st = f"{self.title} ({self.descr}). Duration: {self.duration}"
        st += "\n" + "-" * 20
        for video in self.videos:
            st += "\n" + str(video)
        return st 
        
    def add_video(self, video):
        self.videos += [video]
        
    def recommendation(self):
        return f"Recommendation: {self.videos[randrange(len(self.videos))]}"
        
        
        
class ClassicPlaylist(Playlist):
    def __init__(self, title, descr, duration, videos, period):
        super().__init__(title, descr, duration, videos)
        self.period = period
        
    def recommendation(self):
        return f"Recommendation: {self.videos[0]}!"
        

def main():
    seed(datetime.now())
    p = Playlist("Zouzounia","Children's Songs","45.18",
                [Video("Zouzounia","Love Bees", "03:22"),Video("Zouzounia","Love Animals", "04:22")])
                
    print(p)
    print(p.recommendation())
    c = ClassicPlaylist("Beethoven No.9","Beethoven","88.13",
                        [Video("Beethoven","Symphony No.2", "43:22"),Video("Beethoven","Symphony No.3", "40:02")],"Classical")
    print(c)
    print(p.recommendation())
    
main()
