from django.shortcuts import render
import requests
from collections import defaultdict

def getData(request):

    data = requests.get('https://api.nytimes.com/svc/mostpopular/v2/viewed/1.json?api-key=q1ih70IfPEQqoqVTe73Jfz9pGQyLkACQ').json()['results']


    d = []
    for a in data:
        d.append(a.update({'images' : a['media'][0]['media-metadata'][2]['url']}))




    return render(request,'index.html', {'data' : data})