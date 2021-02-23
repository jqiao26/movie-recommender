from googleapiclient.discovery import build
from mr.data import get_data
from mr.recommendation import get_searched_title
import os
import re


google_api_key = os.environ['GOOGLE_API_KEY']
google_engine_id = os.environ['GOOGLE_ENGINE_ID']


def _google_search(search, api_key=google_api_key, cse_id=google_engine_id):
    '''
    Searches a custom search engine for the movie
    '''
    service = build('customsearch', 'v1', developerKey=api_key)
    res = service.cse().list(q=search, cx=cse_id, searchType='image').execute()
    return res['items']


def get_google_movie_poster(search):
    '''
    Gets the IMDb result and returns the movie poster image and IMDb link
    '''
    results = _google_search(search)

    # Filter out brackets for search (The Prestige (2006) --> the prestige)
    search = re.sub(r"[\(\[].*?[\)\]]", "", search)
    search = search.lower()

    for result in results:
        title = result['title'].lower()
        if search in title and ' - imdb' in title:
            return result['link'], result['image']['contextLink']
    return 'No link', 'No contextLink'


def get_local_poster(movie_name):
    '''
    Searches for a poster
    '''
    mdf, final_dataset, poster_data = get_data()
    real_name = get_searched_title(movie_name)

    try:
        # ind = mdf.loc[mdf['title'].str.contains(real_name)].index[0]
        ind = mdf.loc[mdf['title'] == real_name].index[0]
        poster = poster_data['link'][ind]
        return poster
    except:
        return 'No link'
