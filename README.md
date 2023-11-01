# Chitter Project

## Introduction
This is a project I undertook at the beginning of week 6 of the Makers Academy bootcamp. This is my first web app and first time to use Flask. This is a very simple project and was a great introduction to Flask and also CSS (the CSS isn't very well organised here - if I had time I would tidy it up).
This is a site where a user can simply keep a record of artists and albums. The artsts-albums relation is a one-to-many. If I had more time, I would add a method to find all the songs on an album from another website, and I would also add user accounts and login features.

## Features

- Stores a list of artists with their names and genres
- Displays the list of artists in alphabetical order
- Stores a list of albums with their titles, release dates and artists
- Displays the list of albums according to the alphabetical ordering of the artists' names
- Allows the user to add and delete artists and albums - artists can be added from the 'All Artists' page, and albums can be added from the 'All Albums' page as well as any individual artist's page.

## Key Technologies

- **Backend:** Python, Flask, PostgreSQL
- **Testing:** Playwright

## Database Tables

- ***artists*** (id, name, genre)
- one-to-many with albums through artist_id
- ***albums*** (id, title, release_year, artist_id [FK - artists.id]) - FK connects album to artist

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