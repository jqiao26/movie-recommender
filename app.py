from flask import Flask, request, render_template
from mr.recommendation import get_recommendations
from mr.imager import get_local_poster
from mr.metadata import get_movie_genre
from mr.recommendation import get_searched_title
import re


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/movies', methods=['POST'])
def topic():
    '''
    Give a movie then provide movie suggestions
    '''
    if request.method == 'POST':
        req = request.json
        movie = request.form['input']

        in_mov_poster = get_local_poster(movie)
        mov_genre = get_movie_genre(movie)

        recommendations, posters = get_recommendations(str(movie))
        reco = []
        for rec in recommendations:
            rec = re.sub(r"\(([^0-9]+)\)", "", str(rec))
            reco.append(rec)
        real_movie = get_searched_title(movie)

    return render_template('result.html', in_movie_title=real_movie, in_movie=in_mov_poster, movies=reco, posters=posters, genres=mov_genre, len=len(recommendations))
