from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.core.cache import cache
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Greeting

from lib.classifier import Classifier

@csrf_exempt
def index(request):
    if 'text' not in request.POST:
        return HttpResponse(json.dumps([]), content_type='application/json')

    clf = cache.get('clf')
    if clf == None:
        clf = Classifier()
        # cache the classifier
        cache.set('clf', clf)
    
    emails = request.POST.getlist('text')
    response = clf.classify(emails)
    return HttpResponse(json.dumps(response), content_type='application/json')

