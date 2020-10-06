from django.test import TestCase

# Create your tests here.
import pickle

# url = staticfiles_storage.url('recom/model.pkl')
loaded_model = pickle.load(open("/home/theblankidea/Desktop/TCET/recom_project/recom/static/recom/model.pkl", 'rb'))
loaded_df = pickle.load(open("/home/theblankidea/Desktop/TCET/recom_project/recom/static/recom/dataframe.pkl", 'rb'))

# This is our product ID
# query_index = 3
def predict(product_id):
    query_index = product_id
    distances, indices = loaded_model.kneighbors(loaded_df.iloc[query_index,:].values.reshape(1, -1), n_neighbors = 6)
    for i in range(0, len(distances.flatten())):
        if i == 0:
            print('Recommendations for {0}:\n'.format(loaded_df.index[query_index]))
        else:
            print('{0}: {1} {2}'.format(i, indices[0][1:], loaded_df.index[indices.flatten()[i]]))    
        # Get all the product ids in output and store somewhere ... like list?

    # Now that we have predicted product ids, we query database to fetch pid, name and URL for image.

# predict(200) # zBoost YX-510 Cell Phone Signal Booster
# predict(122) #  Motorola V197 Unlocked Phone with Quad-Band GSM and Bluetooth-International Version
