import os
from flask import Flask, request, redirect, render_template
from lib.database_connection import get_flask_database_connection
from lib.album_repository import *
from lib.album import *
from lib.artist_repository import *
from lib.artist import *


app = Flask(__name__)
app.jinja_env.autoescape = True  # Stops people hacking


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/artists")
def get_artists():
    connection = get_flask_database_connection(app)
    repo = ArtistRepository(connection)
    artists = repo.get_all_artists()
    return render_template('artists.html', artists=sorted(artists, key=lambda artist: artist.name))


@app.route("/albums")
def get_albums():
    connection = get_flask_database_connection(app)
    artist_repo = ArtistRepository(connection)
    album_repo = AlbumRepository(connection)
    albums = album_repo.get_all_albums()
    artists = artist_repo.get_all_artists()
    artist_id_to_name = {artist.id:artist.name for artist in artists}
    sorted_albums_date = sorted(albums, key=lambda album: album.release_year)
    sorted_albums = sorted(sorted_albums_date, key=lambda album: artist_id_to_name[album.artist_id])
    return render_template('albums.html', albums=sorted_albums, artists=artist_id_to_name)


@app.route("/artists/<id>")
def get_single_artist(id):
    connection = get_flask_database_connection(app)
    artist_repo = ArtistRepository(connection)
    album_repo = AlbumRepository(connection)
    artist = artist_repo.find_artist(id)
    albums = album_repo.get_all_albums()
    albums_by_artist = sorted([album for album in albums if album.artist_id == artist.id], key=lambda album: album.release_year)
    delete = request.args.get('delete')
    if len(albums_by_artist) == 0:
        return render_template('single_artist.html', artist=artist, albums=None, delete=delete)
    return render_template('single_artist.html', artist=artist, albums=albums_by_artist, delete=delete)


@app.route("/albums/<id>")
def get_single_album(id):
    connection = get_flask_database_connection(app)
    album_repo = AlbumRepository(connection)
    artist_repo = ArtistRepository(connection)
    album = album_repo.find_album(id)
    artist = artist_repo.find_artist(album.artist_id)
    artist_id = request.args.get('from')
    delete = request.args.get('delete')
    return render_template('single_album.html', album=album, artist=artist, id_for_artist=artist_id, delete=delete)


@app.route("/artists/new", methods=['GET'])
def get_artist_new():
    return render_template('new_artist.html')


@app.route("/artists", methods=['POST'])
def create_artist():
    connection = get_flask_database_connection(app)
    repo = ArtistRepository(connection)

    name = request.form['name']
    genre = request.form['genre']
    artist = Artist(None, name, genre)

    if not artist.is_valid():
        return render_template('new_artist.html', errors=artist.generate_errors())

    repo.create_artist(artist)
    return redirect(f"/artists/{artist.id}")


@app.route("/albums/new", methods=['GET'])
def get_album_new():
    connection = get_flask_database_connection(app)
    artist_repo = ArtistRepository(connection)
    artists = artist_repo.get_all_artists()
    given_artist = request.args.get('given_artist')
    if given_artist == None:
        return render_template('new_album.html', artists=sorted(artists, key=lambda artist: artist.name))
    fixed_artist = [artist for artist in artists if artist.name == given_artist]
    return render_template('new_album.html', artists=fixed_artist)


@app.route("/albums", methods=['POST'])
def create_album():
    connection = get_flask_database_connection(app)
    repo = AlbumRepository(connection)

    title = request.form['title']
    release_year = request.form['release_year']
    artist_id = request.form['artist']
    is_fixed = int(request.form['is_fixed'])
    album = Album(None, title, int(release_year), int(artist_id))

    if not album.is_valid():
        artist_repo = ArtistRepository(connection)
        artists = artist_repo.get_all_artists()
        if is_fixed == 0:
            return render_template('new_album.html', errors=album.generate_errors(), artists=artists)
        fixed_artist = [artist for artist in artists if artist.id == int(artist_id)]
        return render_template('new_album.html', errors=album.generate_errors(), artists=fixed_artist)

    repo.create_album(album)
    return redirect(f"/albums/{album.id}")


@app.route("/delete_artist", methods=['POST'])
def delete_artist():
    delete = request.form['delete']
    id = request.form['id']
    if delete != "Yes":
        return redirect(f"/artists/{id}")
    connection = get_flask_database_connection(app)
    artist_repo = ArtistRepository(connection)
    artist_repo.delete_artist(id)
    return redirect("/artists")


@app.route("/delete_album", methods=['POST'])
def delete_album():
    delete = request.form['delete']
    id = request.form['id']
    id_artist = request.form['id_artist']
    if delete != "Yes":
        return redirect(f"/albums/{id}?from={id_artist}")
    connection = get_flask_database_connection(app)
    album_repo = AlbumRepository(connection)
    album_repo.delete_album(id)
    if id_artist == '0':
        return redirect("/albums")
    return redirect(f"/artists/{id_artist}")


if __name__ == '__main__':
    app.run(
        debug=True,
        host="0.0.0.0",
        port=int(os.environ.get('PORT', 5000))
    )
