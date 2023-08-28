from lib.album import *

class AlbumRepository:

    def __init__(self, connection):
        self._connection = connection
    
    def get_all_albums(self):
        rows = self._connection.execute('SELECT * from albums')
        albums = []
        for row in rows:
            item = Album(row["id"], row["title"], row["release_year"], row["artist_id"])
            albums.append(item)
        return albums
    
    def find_album(self, album_id):
        rows = self._connection.execute('SELECT * from albums WHERE id = %s', [album_id])
        row = rows[0]
        return Album(row["id"], row["title"], row["release_year"], row["artist_id"])
    
    def create_album(self, album):
        rows = self._connection.execute(
            'INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s) RETURNING id',
            [album.title, album.release_year, album.artist_id])
        row = rows[0]
        album.id = row['id']
        return album

    def delete_album(self, album_id):
        self._connection.execute(
            'DELETE FROM albums WHERE id = %s', [album_id]
        )
