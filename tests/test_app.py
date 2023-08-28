from playwright.sync_api import Page, expect

def test_get_artists(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    artist_container = page.locator(".artist-container")
    expect(artist_container).to_have_text([
        "ABBA\nPop",
        "Nina Simone\nJazz",
        "Pixies\nRock",
        "Taylor Swift\nPop"
    ])
    add_artist = page.locator(".add_artist")
    expect(add_artist).to_have_text("Add New Artist")


def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    album_container = page.locator(".album-container")
    expect(album_container).to_have_text([
        "Ring Ring\nABBA\n1973",
        "Waterloo\nABBA\n1974",
        "Super Trouper\nABBA\n1980",
        "I Put a Spell on You\nNina Simone\n1965",
        "Here Comes the Sun\nNina Simone\n1971",
        "Baltimore\nNina Simone\n1978",
        "Fodder on My Wings\nNina Simone\n1982",
        "Surfer Rosa\nPixies\n1988",
        "Doolittle\nPixies\n1989",
        "Bossanova\nPixies\n1990",
        "Lover\nTaylor Swift\n2019",
        "Folklore\nTaylor Swift\n2020"
    ])
    add_album = page.locator(".add_album")
    expect(add_album).to_have_text("Add New Album")

def test_get_single_artist(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists/3")
    name = page.locator(".t-name")
    expect(name).to_have_text(["Taylor Swift"])
    genre = page.locator(".t-genre")
    expect(genre).to_have_text(["Genre: Pop"])
    albums = page.locator(".t-albums")
    expect(albums).to_have_text(["Albums:\nLover (2019)\nFolklore (2020)"])
    bottom_buttons = page.locator(".bottom-buttons")
    expect(bottom_buttons).to_have_text(["Add Album\nDelete Artist"])

def test_get_single_album(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums/9")
    title = page.locator(".t-title")
    expect(title).to_have_text(["Baltimore"])
    release_year = page.locator(".t-release-year")
    expect(release_year).to_have_text(["Released: 1978"])
    artist = page.locator(".t-artist")
    expect(artist).to_have_text(["Artist: Nina Simone"])
    bottom_buttons = page.locator(".bottom-buttons")
    expect(bottom_buttons).to_have_text(["Delete Album"])

def test_get_artist_new_create_artist_successful_finish(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text='Add New Artist'")
    page.fill("input[name=name]", "Bonjovi")
    page.select_option("select[name=genre]", value='Rock')
    page.click("text='Add Artist'")
    
    name = page.locator(".t-name")
    expect(name).to_have_text(["Bonjovi"])
    genre = page.locator(".t-genre")
    expect(genre).to_have_text(["Genre: Rock"])
    albums = page.locator(".t-albums")
    expect(albums).to_have_text(["Albums:\nNo albums added yet."])
    bottom_buttons = page.locator(".bottom-buttons")
    expect(bottom_buttons).to_have_text(["Add Album\nDelete Artist"])

def test_get_artist_new_create_artist_error_name(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text='Add New Artist'")
    page.fill("input[name=name]", "")
    page.select_option("select[name=genre]", value='Rock')
    page.click("text='Add Artist'")

    error = page.locator(".t-errors")
    expect(error).to_have_text(["! Please enter a name for the artist !"])

def test_get_artist_new_create_artist_error_name_genre(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text='Add New Artist'")
    page.click("text='Add Artist'")

    error = page.locator(".t-errors")
    expect(error).to_have_text(["! Please enter a name for the artist !\n! Please enter a genre for the artist !"])

def test_delete_artist_yes(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text='ABBA'")
    page.click("text='Delete Artist'")
    page.click("text='Yes'")

    artist_container = page.locator(".artist-container")
    expect(artist_container).to_have_text([
        "Nina Simone\nJazz",
        "Pixies\nRock",
        "Taylor Swift\nPop"
    ])
    add_artist = page.locator(".add_artist")
    expect(add_artist).to_have_text("Add New Artist")
    page.click("text='All Albums'")

    album_container = page.locator(".album-container")
    expect(album_container).to_have_text([
        "I Put a Spell on You\nNina Simone\n1965",
        "Here Comes the Sun\nNina Simone\n1971",
        "Baltimore\nNina Simone\n1978",
        "Fodder on My Wings\nNina Simone\n1982",
        "Surfer Rosa\nPixies\n1988",
        "Doolittle\nPixies\n1989",
        "Bossanova\nPixies\n1990",
        "Lover\nTaylor Swift\n2019",
        "Folklore\nTaylor Swift\n2020"
    ])
    add_album = page.locator(".add_album")
    expect(add_album).to_have_text("Add New Album")

def test_delete_artist_no(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text='Taylor Swift'")
    page.click("text='Delete Artist'")
    page.click("text='No'")

    name = page.locator(".t-name")
    expect(name).to_have_text(["Taylor Swift"])
    genre = page.locator(".t-genre")
    expect(genre).to_have_text(["Genre: Pop"])
    albums = page.locator(".t-albums")
    expect(albums).to_have_text(["Albums:\nLover (2019)\nFolklore (2020)"])
    bottom_buttons = page.locator(".bottom-buttons")
    expect(bottom_buttons).to_have_text(["Add Album\nDelete Artist"])

def test_get_album_new_create_album_successful_finish(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Add New Album'")
    page.fill("input[name=title]", "Delightful Joy")
    page.select_option("select[name=release_year]", value='1999')
    page.select_option("select[name=artist]", value='Taylor Swift')
    page.click("text='Add Album'")
    
    title = page.locator(".t-title")
    expect(title).to_have_text(["Delightful Joy"])
    release_year = page.locator(".t-release-year")
    expect(release_year).to_have_text(["Released: 1999"])
    artist = page.locator(".t-artist")
    expect(artist).to_have_text(["Artist: Taylor Swift"])
    bottom_buttons = page.locator(".bottom-buttons")
    expect(bottom_buttons).to_have_text(["Delete Album"])

def test_get_album_new_create_album_error_artist(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Add New Album'")
    page.fill("input[name=title]", "Delightful Joy")
    page.select_option("select[name=release_year]", value='1999')
    page.click("text='Add Album'")
    
    error = page.locator(".t-errors")
    expect(error).to_have_text(["! Please select an artist !"])

def test_get_album_new_create_album_error_title_release_year_artist(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Add New Album'")
    page.fill("input[name=title]", "")
    page.click("text='Add Album'")
    
    error = page.locator(".t-errors")
    expect(error).to_have_text(["! Please enter an album title !\n! Please select a year !\n! Please select an artist !"])

def test_get_album_new_successful_finish_from_artist_page(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text='Nina Simone'")
    page.click("text='Add Album'")
    page.fill("input[name=title]", "A Wonderful World")
    page.select_option("select[name=release_year]", value='1986')
    page.click("text='Add Album'")
    
    title = page.locator(".t-title")
    expect(title).to_have_text(["A Wonderful World"])
    release_year = page.locator(".t-release-year")
    expect(release_year).to_have_text(["Released: 1986"])
    artist = page.locator(".t-artist")
    expect(artist).to_have_text(["Artist: Nina Simone"])
    bottom_buttons = page.locator(".bottom-buttons")
    expect(bottom_buttons).to_have_text(["Delete Album"])

def test_get_album_new_error_title_release_year_artist(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Pixies'")
    page.click("text='Add Album'")
    page.click("text='Add Album'")
    
    error = page.locator(".t-errors")
    expect(error).to_have_text(["! Please enter an album title !\n! Please select a year !"])

def test_delete_album_yes_from_single_artist_page(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text='ABBA'")
    page.click("text='Super Trouper'")
    page.click("text='Delete Album'")
    page.click("text='Yes'")

    name = page.locator(".t-name")
    expect(name).to_have_text(["ABBA"])
    genre = page.locator(".t-genre")
    expect(genre).to_have_text(["Genre: Pop"])
    albums = page.locator(".t-albums")
    expect(albums).to_have_text(["Albums:\nRing Ring (1973)\nWaterloo (1974)"])
    bottom_buttons = page.locator(".bottom-buttons")
    expect(bottom_buttons).to_have_text(["Add Album\nDelete Artist"])

    page.click("text='All Albums'")

    album_container = page.locator(".album-container")
    expect(album_container).to_have_text([
        "Ring Ring\nABBA\n1973",
        "Waterloo\nABBA\n1974",
        "I Put a Spell on You\nNina Simone\n1965",
        "Here Comes the Sun\nNina Simone\n1971",
        "Baltimore\nNina Simone\n1978",
        "Fodder on My Wings\nNina Simone\n1982",
        "Surfer Rosa\nPixies\n1988",
        "Doolittle\nPixies\n1989",
        "Bossanova\nPixies\n1990",
        "Lover\nTaylor Swift\n2019",
        "Folklore\nTaylor Swift\n2020"
    ])
    add_album = page.locator(".add_album")
    expect(add_album).to_have_text("Add New Album")

def test_delete_album_yes_from_albums_page(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Super Trouper'")
    page.click("text='Delete Album'")
    page.click("text='Yes'")

    album_container = page.locator(".album-container")
    expect(album_container).to_have_text([
        "Ring Ring\nABBA\n1973",
        "Waterloo\nABBA\n1974",
        "I Put a Spell on You\nNina Simone\n1965",
        "Here Comes the Sun\nNina Simone\n1971",
        "Baltimore\nNina Simone\n1978",
        "Fodder on My Wings\nNina Simone\n1982",
        "Surfer Rosa\nPixies\n1988",
        "Doolittle\nPixies\n1989",
        "Bossanova\nPixies\n1990",
        "Lover\nTaylor Swift\n2019",
        "Folklore\nTaylor Swift\n2020"
    ])
    add_album = page.locator(".add_album")
    expect(add_album).to_have_text("Add New Album")

def test_delete_album_no(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text='Pixies'")
    page.click("text='Doolittle'")
    page.click("text='Delete Album'")
    page.click("text='No'")

    title = page.locator(".t-title")
    expect(title).to_have_text(["Doolittle"])
    release_year = page.locator(".t-release-year")
    expect(release_year).to_have_text(["Released: 1989"])
    artist = page.locator(".t-artist")
    expect(artist).to_have_text(["Artist: Pixies"])
    bottom_buttons = page.locator(".bottom-buttons")
    expect(bottom_buttons).to_have_text(["Delete Album"])
