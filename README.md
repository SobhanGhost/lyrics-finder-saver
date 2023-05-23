# lyrics-finder-saver
a python script which using an Genius API, finds lyrics of the songs of a directory and saves them.

required modules:
1. lyricsgenius
2. music_tag

to install the modules, open cmd, type in "pip install 'module_name'" and Enter.

To use, you need to enter a directory that contains songs with standard names; Standard name is like this:
Single Song:
  "Artist" - "Song_Title" (Ft "Featuring Artists")
  e.g:
  Lil Wayne - Believe Me (Ft Drake)
Album Song:
  "Track_Number" "Song_Title" (Ft "Featuring Artists")
  e.g:
  05 Righteous

However, any mp3 track has some attributes like "title", "artist" and etc., therefore these attributes need to be standard and correct.
e.g the song "Righteous" by "Juice WRLD" needs its "title" attr to be "Righteous" and its "artist" to be "Juice WRLD".
