import music_tag as m
from lyricsgenius import Genius
import os


api="apOmJ1qNDXoveYmug-MY-TaiuAKI3O-muQH4iABbTmyyE_tJK5BAqolYBX7-gQYp"

g=Genius(api)

artists={}

while True:

    add=input("Enter the directory address:\n")
    if add == "":
        break
    try:
        os.chdir(add)
    except:
        print("Directory does not exists.")
        continue
    files=os.listdir()
    
    for file in files:
        
        if ".mp3" in file :
            track=m.load_file(add+"\\"+file)
            title = str(track["title"])
            while True:
                try:
                
                    song=g.search_song(track["title"].value,track["artist"].value
                                       )
                    break
                except:
                    
                    continue
            if song==None:
                continue
            track["lyrics"]=song.lyrics
            track.save()
