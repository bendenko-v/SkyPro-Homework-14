# SkyPro / Homework 14

SQL queries

## Usage

Run "main.py" to start the Flask app.

## App features

* On the main page "/" displays a search field. You can search movies/TV shows from the database.
* The '/movie/title' view returns a JSON with movies/TV shows by name.
* The '/movie/from_year/to/to_year>' view returns a JSON with movies/TV shows by years.
* The "/rating/grade" view returns a JSON with movies/TV shows by rating (the grade can be "child", "family", "adult").
* The '/genre/genre' view returns a JSON with top 10 latest movies/TV shows by genre.
* The '/actors' view returns a list of actors who played with Jack Black, Dustin Hoffman in 2 or more films.
* The '/getmovies' view returns a JSON with movies/TV shows data from funtion with parameters 'type', 'year', 'genre'.
* If you try to get a page that doesn't exist, a 404 error will be applied.
