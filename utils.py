import sqlite3


def get_data_from_db(query):
    with sqlite3.connect("netflix.db") as db:
        cur = db.cursor()
        cur.execute(query)
        result = cur.fetchall()
        return result


def get_movies_by_name(movie_title):
    query = (
        "SELECT title, country, release_year, listed_in, description "
        "FROM netflix "
        f"WHERE title LIKE '%{movie_title}%' "
        "ORDER BY release_year DESC"
    )

    result = get_data_from_db(query)
    movies = []
    if result:
        for movie in result:
            movies.append({'title': movie[0],
                           'country': movie[1],
                           'release_year': movie[2],
                           'genre': movie[3],
                           'description': movie[4]
                           })
    return movies


def get_movies_by_years(from_, to_):
    query = (
        "SELECT title, release_year "
        "FROM netflix "
        f"WHERE release_year BETWEEN {from_} AND {to_} "
        "ORDER BY release_year DESC "
        "LIMIT 100"
    )

    result = get_data_from_db(query)
    movies = []
    if result:
        for movie in result:
            movies.append({'title': movie[0],
                           'release_year': movie[1]
                           })
    return movies


def get_movies_by_rating(rating_name):
    match rating_name:
        case 'children':
            grade = ('G', '')
        case 'family':
            grade = ('G', 'PG', 'PG-13')
        case 'adult':
            grade = ('R', 'NC-17')
        case _:
            grade = ''

    query = (
        "SELECT title, rating, description "
        "FROM netflix "
        "WHERE rating != '' "
        f"AND rating IN {grade} "
        "ORDER BY rating"
    )

    result = get_data_from_db(query)
    movies = []
    if result:
        for movie in result:
            movies.append({'title': movie[0],
                           'rating': movie[1],
                           'description': movie[2],
                           })
    return movies


def get_movies_by_genre(genre):
    query = (
        "SELECT title, description "
        "FROM netflix "
        f"WHERE listed_in LIKE '%{genre}%' "
        "ORDER BY release_year DESC "
        "LIMIT 10"
    )

    result = get_data_from_db(query)
    movies = []
    if result:
        for movie in result:
            movies.append({'title': movie[0],
                           'description': movie[1]
                           })
    return movies


def get_movies_by_actors(actors_):
    query = (
        "SELECT DISTINCT netflix.cast "
        "FROM netflix "
        f"WHERE netflix.cast LIKE '%{actors_[0]}%' "
        f"AND netflix.cast LIKE '%{actors_[1]}%'"
    )

    result = get_data_from_db(query)
    actors = set(actors_)
    cast_together = []
    for data in result:
        for actor in data[0].split(', '):
            if actor not in actors:
                actors.add(actor)
            elif actor not in cast_together and actor not in actors_:
                cast_together.append(actor)

    return cast_together


def get_movies_type_year_genre(type_, year, genre):
    query = (
        "SELECT title, description, release_year "
        "FROM netflix "
        f"WHERE type = '{type_}' "
        f"AND release_year = '{year}' "
        f"AND listed_in LIKE '%{genre}%'"
    )

    result = get_data_from_db(query)
    movies = []
    if result:
        for movie in result:
            movies.append({'title': movie[0],
                           'description': movie[1]
                           })
    return movies
