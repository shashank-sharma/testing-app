from django.shortcuts import render
from home.models import Form
from django.http import Http404, HttpResponse
import json
import csv

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def data(request):
    if request.is_ajax():
        name = request.GET['name']
        address = request.GET['address']
        email = request.GET['email']
        try:
            formModel = Form(username = name, address = address, email = email)
            formModel.save()
            temp = 'yes'
        except:
            temp = 'no'
        data = json.dumps(temp)
        return HttpResponse(data, content_type = "application/json")
    else:
        raise Http404

def suggestionName(request):
    if request.is_ajax():
        keyword = request.GET['keyword']
        temp = []
        with open('static/data/Indian-Male-Names.csv') as csvfile:
            read = csv.reader(csvfile, delimiter = ' ', quotechar = '|')
            for row in read:
                word = row[0].split(',')[0]
                if keyword == word[:len(keyword)]:
                    temp.append(word)
        temp = list(set(temp))
        data = json.dumps(temp)
        return HttpResponse(data, content_type = "application/json")
    else:
        raise Http404
