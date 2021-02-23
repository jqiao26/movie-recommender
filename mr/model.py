import pickle


def load_csr_data():
    '''
    Loads CSR sparse matrix
    '''
    pickle_filename = './notebooks/csr_data.pickle'

    with open(pickle_filename, 'rb') as f:
        csr_data = pickle.load(f)
    return csr_data


def load_model():
    '''
    Loads KNN recommender model
    '''
    pickle_filename = './notebooks/knn_recommender.pickle'

    with open(pickle_filename, 'rb') as f:
        knn = pickle.load(f)
    return knn
    