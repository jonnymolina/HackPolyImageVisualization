from django.shortcuts import render
from django.template import Context, loader
from django.http import HttpResponse
from django.conf import settings
from django.middleware import csrf
from django.views.decorators.csrf import *
from clarifai.client import ClarifaiApi
from firebase import firebase
import StringIO
import os, requests, json, os.path

clarifai_id = settings.CLARIFAI_ID
clarifai_secret = settings.CLARIFAI_SECRET

os.environ['CLARIFAI_ID'] = clarifai_id
os.environ['CLARIFAI_SECRET'] = clarifai_secret
clarifai_api = ClarifaiApi(app_id = clarifai_id, app_secret = clarifai_secret)

MEDIA_URL =  settings.MEDIA_URL
array_of_urls = []

def index(request):
    #array of urls = get all firebase children
    #test = all urls
    #render from test
    print "csrf: " + csrf.get_token(request)
    template = loader.get_template('index.html')
    test = "poo"
    context = Context({'MEDIA_URL' : MEDIA_URL, 'test': test})
    return HttpResponse(template.render(context))

#set up the initial entry
@csrf_exempt
def setup(request):
    print "request" + str(request)
    result = request.method
    print "result: " + str(result)
    if result == "POST":
        #initialize
        array_of_urls = []
        fb = firebase.FirebaseApplication('https://hackpolyvisual.firebaseio.com/', None)
        result = fb.delete('/', None)
        print(result)
        #if result == None:
            #return HttpResponse("{'status':'405 - didnt delete'}", content_type="application/json")
        # set up db entry
        # qstr = request.raw_post_data
        # print "qstr: " + str(qstr)
        # config = json.loads(str(qstr))
        # print "config: " + config
        # url = config["url"]
        url = "https://www.petfinder.com/wp-content/uploads/2012/11/dog-how-to-select-your-new-best-friend-thinkstock99062463.jpg"
        print "url: " + url
        
        array_of_urls.append(url)
        depth = 0
        tags = [] #get tags from function
        name = "dog" #get first tage
        parentId = 1
        result = fb.post('/', str(parentId),
            {'depth':str(depth),'url':str(url)})
            #{'parentId':parentId},
            #{'tags':str(tags)},
            #{'url':str(url)})
        print "result2: " + result
        if result == None:
            return HttpResponse("{'status':'405 - didnt add'}", content_type="application/json")
    template = loader.get_template('setup.html')
    return HttpResponse(template.render(request))





def clarifai(request):
    url = request.GET.get("url")
    test = "poo"
    template = loader.get_template('clarifai.html')
    context = Context({'MEDIA_URL' : MEDIA_URL, 'count': 10})
    return HttpResponse(template.render(context))

#def add(request):
    #check if url is in array
        #if not add to firebase and to array of urls

#def clear(request):
    #firebase = none