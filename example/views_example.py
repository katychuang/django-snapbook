from instagram.client import InstagramAPI
import flickrapi, tweepy, simplejson, urllib
import re

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.template import loader, Context
from django.contrib.flatpages.models import FlatPage
from django.db.models import Q
from django.template import RequestContext


def flickr(request):
    api_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    api_secret = 'YYYYYYYYYYYYYYYY'

    flickr = flickrapi.FlickrAPI(api_key, api_secret, format='json')

    #pass to template
    return render_to_response("example/index.html", {'twitters': flickr})


def instagram(request):
    api = InstagramAPI(client_id='CLIENT_ID',
                       client_secret='CLIENT_SECRET_KEY')

    #get popular images
    popular_media = api.media_popular(count=20)

    #add popular images
    p = []
    for media in popular_media:
        print media.images['standard_resolution'].url
        p.append(media.images['standard_resolution'].url)

    #pass to template
    return render_to_response("example/index.html", {'popular': p})


def tumblr(request):
    tag = "fashion"
    api_key = "API_KEY"
    t = "http://api.tumblr.com/v2/tagged?api_key=%stag=%s".format(api_key, tag)
    return render_to_response("example/index.html",
                              {'twitters': t,
                               'page_title': 'Photos from Tumblr'})


def tweets(request):
    api = twitter.Api(consumer_key='consumer_key',
                      consumer_secret='consumer_secret',
                      access_token_key='access_token',
                      access_token_secret='access_token_secret')
    #print api.VerifyCredentials()

    #pass to template
    return render_to_response("example/index.html", {'twitters': ''})

def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    ''' Splits the query string in invidual keywords, getting rid of unecessary spaces
        and grouping quoted words together.
        Example:

        >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']

    '''
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]


def get_query(query_string, search_fields):
    ''' Returns a query, that is a combination of Q objects. That combination
        aims to search keywords within a model by testing the given search fields.

    '''
    query = None  # Query to search for every search term
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None  # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query


def search(request):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']

        api_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        tumblr = 'http://api.tumblr.com/v2/tagged?api_key={0}&tag={1}'.format(api_key, query_string)

        nyt_api = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        nyt = "http://api.nytimes.com/svc/search/v1/article?format=json&query={0}&api-key={1}".format(query_string,nyt_api)

        pearson_api = "191974694fb48173856e0f213e19a413"
        pearson = "http://api.pearson.com/v2/dictionaries/entries?headword="+query_string+"&apikey="+pearson_api
        resultP = simplejson.load(urllib.urlopen(pearson))

        try:
            definition = resultP['results'][0]['senses'][0]['definition']
        except:
            definition = "DNE"  # definition does not exist

        try:
            pos = resultP['results'][0]['part_of_speech']
        except:
            pos = ""

        n = []
        result1 = simplejson.load(urllib.urlopen(nyt))
        #print result1
        for p in result1['results']:
            try:
                title = p['title']
                author = p['byline']
                body = p['body']
                u = p['url']
                n.append({'title': title, 'author': author, 'body': body, 'url': u})
            except:
                pass

        t = []
        result2 = simplejson.load(urllib.urlopen(tumblr))
        for p in result2['response']:

            if ('photos' in p):
                x = p['photos']
                for item in x:
                    alt = item['alt_sizes']
                    thumbnail = alt[1]['url']
                    t.append(thumbnail)

    return render_to_response('example/index.html',
                              {'query_string': query_string, 'tumble': t, 'nyt': n, 'pos': pos, 'definition': definition},
                              context_instance=RequestContext(request))
