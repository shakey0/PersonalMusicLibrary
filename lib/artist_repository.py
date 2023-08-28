from lib.artist import Artist

class ArtistRepository:

    def __init__(self, connection):
        self._connection = connection

    def get_all_artists(self):
        rows = self._connection.execute('SELECT * from artists')
        artists = []
        for row in rows:
            item = Artist(row["id"], row["name"], row["genre"])
            artists.append(item)
        return artists

    def find_artist(self, artist_id):
        rows = self._connection.execute(
            'SELECT * from artists WHERE id = %s', [artist_id])
        row = rows[0]
        return Artist(row["id"], row["name"], row["genre"])

    def create_artist(self, artist):
        rows = self._connection.execute('INSERT INTO artists (name, genre) VALUES (%s, %s) RETURNING id',
                                        [artist.name, artist.genre])
        row = rows[0]
        artist.id = row['id']
        return artist

    def delete_artist(self, artist_id):
        self._connection.execute(
            'DELETE FROM artists WHERE id = %s', [artist_id])
