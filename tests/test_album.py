from lib.album import *

def test_album_constructs():
    album = Album(2, "Test Album", 1980, 4)
    assert album.id == 2
    assert album.title == "Test Album"
    assert album.release_year == 1980
    assert album.artist_id == 4

def test_album_formats_nicely():
    album = Album(1, "Test Album", 4000, 5)
    assert str(album) == "Album(1, Test Album, 4000, 5)"

def test_albums_are_equal():
    album1 = Album(2, "Nice Day", 3500, 3)
    album2 = Album(2, "Nice Day", 3500, 3)
    assert album1 == album2