from django.contrib.staticfiles.storage import staticfiles_storage
from django.shortcuts import render
from django.http import HttpResponse
from recom.models import Product

import pickle

# url = staticfiles_storage.url('recom/model.pkl')
loaded_model = pickle.load(open("model.pkl", 'rb'))
loaded_df = pickle.load(open("dataframe.pkl", 'rb'))

# Create your views here.
def index(request):
    return render(request, "recom/index.html")

def predict(request, product_id):
    query_index = product_id
    distances, indices = loaded_model.kneighbors(loaded_df.iloc[query_index,:].values.reshape(1, -1), n_neighbors = 6)

    product_fetch_list = indices[0][1:]
    products = []

    for i in product_fetch_list:
        p = Product.objects.get(pid=i)
        products.append(p)

    return render(request, "recom/index.html", {
        "products": products,
        })
