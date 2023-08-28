from lib.artist_repository import ArtistRepository
from lib.artist import Artist

def test_get_all_records(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = ArtistRepository(db_connection)

    artists = repository.get_all_artists()

    assert artists == [
        Artist(1, "Pixies", "Rock"),
        Artist(2, "ABBA", "Pop"),
        Artist(3, "Taylor Swift", "Pop"),
        Artist(4, "Nina Simone", "Jazz"),
    ]

def test_get_single_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = ArtistRepository(db_connection)

    artist = repository.find_artist(3)
    assert artist == Artist(3, "Taylor Swift", "Pop")

def test_create_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = ArtistRepository(db_connection)

    repository.create_artist(Artist(None, "The Beatles", "Rock"))

    result = repository.get_all_artists()
    assert result == [
        Artist(1, "Pixies", "Rock"),
        Artist(2, "ABBA", "Pop"),
        Artist(3, "Taylor Swift", "Pop"),
        Artist(4, "Nina Simone", "Jazz"),
        Artist(5, "The Beatles", "Rock"),
    ]

def test_delete_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = ArtistRepository(db_connection)
    repository.delete_artist(3)

    result = repository.get_all_artists()
    assert result == [
        Artist(1, "Pixies", "Rock"),
        Artist(2, "ABBA", "Pop"),
        Artist(4, "Nina Simone", "Jazz"),
    ]
