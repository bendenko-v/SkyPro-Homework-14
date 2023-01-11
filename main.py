from flask import Flask, render_template, request, jsonify
from utils import *

app = Flask(__name__)


@app.route('/')
def index():
    s = request.args.get('s')
    is_search = False

    if s:
        return render_template('index.html',
                               title=f'Search for "{s}"',
                               movie_data=get_movies_by_name(s),
                               is_search=True
                               )

    return render_template('index.html',
                           title='Search movie',
                           is_search=is_search
                           )


@app.route('/movie/<title>')
def movie(title):
    return jsonify(get_movies_by_name(title))
    # return render_template('index.html',
    #                        title=title,
    #                        is_search=True,
    #                        movie_data=get_movies_by_name(title)
    #                        )


@app.route('/movie/<int:from_year>/to/<int:to_year>')
def movies_from_to_years(from_year, to_year):
    return jsonify(get_movies_by_years(from_year, to_year))
    # title = f'Movies from {from_year} to {to_year}'
    # return render_template('index.html',
    #                        title=title,
    #                        is_search=True,
    #                        movie_data=get_movies_by_name(from_year, to_year)
    #                        )


@app.route('/rating/<grade>')
def movies_with_rating(grade):
    return jsonify(get_movies_by_rating(grade))
    # return render_template('index.html',
    #                        title=f'Movies by grade "{grade}"',
    #                        is_grade=True,
    #                        movie_data=get_movies_by_rating(grade)
    #                        )


@app.route('/genre/<genre>')
def movies_by_genre(genre):
    return jsonify(get_movies_by_genre(genre))


@app.route('/actors')
def movies_by_actors():
    return get_movies_by_actors(('Jack Black', 'Dustin Hoffman'))


@app.route('/getmovies')
def movies_by_type_year_genre():
    return jsonify(get_movies_type_year_genre('TV Show', 2020, 'comedy'))


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', title='404 Not found'), 404


@app.errorhandler(500)
def render_server_error(error):
    return render_template('500.html', title='500 Internal Server Error'), 500


if __name__ == '__main__':
    app.run(debug=True)
