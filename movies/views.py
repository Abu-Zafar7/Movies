from django.http import HttpResponse
from django.shortcuts import render

data = {"movies":[
    {
      "id": 1,
      "title": "Dabangg",
      "year": 2011
    },
    {
       "id": 2,
      "title": "Wanted",
      "year": 2013
    },
    {
      "id": 1,
      "title": "DDLJ",
      "year": 1999
    }   
]
}

def movies(request):
    return render(request,"movies\movies.html", data)


def homepage(request):
    return HttpResponse("HOME PAGE")