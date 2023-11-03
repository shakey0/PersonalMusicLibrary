# Personal Music Library

## Introduction
In week 6 of the Makers Academy bootcamp, I dived into web development, crafting my first-ever web app using Flask. This simple platform lets users record and track their favorite artists and albums, underlining the one-to-many relationship between artists and their albums.

Though my initial foray into CSS needs some polishing, the app's simplicity showcases my foundational skills from the beginning of my learning journey.
If I had more time I would:
- Implement a feature that fetches the songs for any given album from an external source.
- Incorporate user account management, allowing for personalized record-keeping and secure logins.

## Features

- Stores a list of artists with their names and genres
- Displays the list of artists in alphabetical order
- Stores a list of albums with their titles, release dates and artists
- Displays the list of albums according to the alphabetical ordering of the artists' names
- Allows the user to add and delete artists and albums - artists can be added from the 'All Artists' page, and albums can be added from the 'All Albums' page as well as any individual artist's page.

## Key Technologies

- **Backend:** Python, Flask, PostgreSQL
- **Frontend:** CSS, HTML
- **Testing:** Playwright

## Database Tables

- **artists** (id, name, genre) - <em>one-to-many with albums through artist_id</em>
- **albums** (id, title, release_year, artist_id [FK - artists.id]) - FK connects album to artist

## Installation & Setup

Run the following command to clone the repo:
```bash
git clone https://github.com/shakey0/PersonalMusicLibrary
cd PersonalMusicLibrary
```

Create your virtual environment:
```bash
pipenv install
pipenv shell
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Run the following commands to create the dev and test databases:
```bash
createdb music_library
createdb music_library_test
python seed_dev_database.py
```

Run the tests:
```bash
pytest
```

Start the server:
```bash
python app.py
```