from mr.data import get_data
from mr.recommendation import get_searched_title


def get_movie_genre(movie):
    '''
    Gets the genres of the movie
    '''
    mdf, final_dataset, poster_data = get_data()
    real_movie = get_searched_title(movie)

    try:
        # ind = mdf.loc[mdf['title'].str.contains(movie)].index[0]
        ind = mdf.loc[mdf['title'] == real_movie].index[0]
        genre_string = mdf['genres'][ind]
        return genre_string.split("|")
    except:
        return 'No genres'
