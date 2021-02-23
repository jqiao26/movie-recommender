from mr.model import load_csr_data
from mr.model import load_model
from mr.data import get_data
import pandas as pd


def get_searched_title(movie_name):
    mdf, final_dataset, poster_data = get_data()
    
    movie_list = mdf[mdf['title'].str.contains('(?i)' + movie_name)]
    movie_name = movie_list.iloc[0]['title']

    return movie_name


def get_recommendations(movie_name):
    '''
    Uses a KNN model to find similar movies to movie_name
    Outputs a list of n recommended movies
    '''
    csr_data = load_csr_data()
    knn = load_model()
    mdf, final_dataset, poster_data = get_data()
    
    n = 12
    real_name = get_searched_title(movie_name)
    movie_list = mdf[mdf['title'] == real_name]
    
    if len(movie_list):
        # TODO: Get the movie poster links and context
        movie_idx = movie_list.iloc[0]['movieId']
        movie_idx = final_dataset[final_dataset['movieId'] == movie_idx].index[0]
        distances , indices = knn.kneighbors(csr_data[movie_idx],n_neighbors=n+1)    
        rec_movie_indices = sorted(list(zip(indices.squeeze().tolist(),distances.squeeze().tolist())),key=lambda x: x[1])[:0:-1]

        recommend_list = []
        posters = []
        for val in rec_movie_indices:
            movie_idx = final_dataset.iloc[val[0]]['movieId']
            idx = mdf[mdf['movieId'] == movie_idx].index

            recommend_list.append(mdf.iloc[idx]['title'].values[0])
            posters.append(poster_data['link'][idx[0]])

        return recommend_list, posters

    else:
        return [], []
