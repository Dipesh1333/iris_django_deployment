from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from .models import PredResults

# Create your views here.
def predict(request):
    return render(request, 'predict.html')

def predict_chances(request):

    # we check if the request is HTML post request
    if request.POST.get('action') == 'post':

        # if it is post request then, receive data from client
        # or collect the data from the post info.

        # the variables 'sepal_length' we have created in predict.html and put that into post message
        # so here we are referencing those variables again and we are just extracting that out and putting in some more variables
        # and we get the info. that the person has typed in.
        sepal_length = float(request.POST.get('sepal_length'))
        sepal_width = float(request.POST.get('sepal_width'))
        petal_length = float(request.POST.get('petal_length'))
        petal_width = float(request.POST.get('petal_width'))

        # Unpickle the model and putting/collecting that data in the model variable
        model = pd.read_pickle(r"new_model.pickle")

        # Make new prediction (with the data we get from the users) using the pretrained model
        result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])

        # saving the predictions in a new variable
        classification = result[0]

        PredResults.objects.create(sepal_length=sepal_length, sepal_width=sepal_width, petal_length=petal_length,
                                    petal_width=petal_width, classification=classification)

        # sending back(to the page) the info. about classification/result/prediction along with the data that the user has typed in
        return JsonResponse({'result': classification, 'sepal_length': sepal_length,
                                'sepal_width': sepal_width, 'petal_length': petal_length, 'petal_width': petal_width},
                            safe=False)


def view_results(request):
    # Submit prediction and show all
    data = {"dataset": PredResults.objects.all()}
    return render(request, "results.html", data)
