from django.shortcuts import render_to_response, get_object_or_404
from instagram.client import InstagramAPI
# import twitter, tweetstream
import tweepy, simplejson, urllib
import flickrapi
#import img_downloader, image_list
from django.http import HttpResponse
from django.template import loader, Context
from django.contrib.flatpages.models import FlatPage
from django.db.models import Q
from django.template import RequestContext
import re

from base_settings import *
from example.models import *


def home(request):

    return render_to_response("example/index.html", {'page_title': 'django-snapbook', 'name': 'home', 'fonts': list(Style.objects.all())})


def flickr(request):
    # url = 'http://api.flickr.com/services/rest/'
    # method = 'flickr.groups.pools.getPhotos'
    api_key = FLICKR_API_KEY
    api_secret = FLICKR_API_SECRET

    flickr = flickrapi.FlickrAPI(api_key, api_secret, format='json')
    photos = flickr.photos_search(user_id='73509078@N00', per_page='10')

#    print result

    t = []
    for item in result['photos']['photo']:
        src = "http://farm{0}.staticflickr.com/{1}/{2}_{3}.jpg".format(item['farm'], item['server'], item['id'], item['secret'])
        t.append(src)

    return render_to_response("example/index.html", {'popular': t, 'page_title': 'Photos from Flickr'})


def grams(request):
    api = InstagramAPI(client_id=INSTAGRAM_CLIENT_ID,
                       client_secret=INSTAGRAM_CLIENT_SECRET)

    #get popular images
    popular_media = api.media_popular(count=20)

    #add popular images
    p = []
    for media in popular_media:
        p.append(media.images['standard_resolution'].url)

    #pass to template
    return render_to_response("example/index.html",
            {'popular': p, 'page_title': 'Top photos from Instagram'})


def tumblr(request):
    tag = "fashion"
    api_key = TUMBLR_API_KEY
    tumblr= 'http://api.tumblr.com/v2/tagged?api_key={0}&tag={1}'.format(api_key, tag)

    t = []
    result2 = simplejson.load(urllib.urlopen(tumblr))
    for p in result2['response']:

        if ('photos' in p):
            x = p['photos']
            for item in x:
                imgpath = item['original_size']['url']
                alt = item['alt_sizes']
                thumbnail = alt[1]['url']  # len(alt)-3
                t.append(imgpath)

    return render_to_response("example/index.html",
                              {'popular': t, 'page_title': 'Photos from tumblr tagged with #fashion'}
                              )


def tweets(request):
    consumer_key = TWITTER_CONSUMER_KEY
    consumer_secret = TWITTER_CONSUMER_SECRET
    key = TWITTER_KEY
    secret = TWITTER_SECRET

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(key, secret)
    api = tweepy.API(auth)

    t = []

    return render_to_response("example/index.html",
                              {'twitters': t, 'page_title': 'Photos from Twitter'})


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

        api_key = TUMBLR_API_KEY
        tumblr = 'http://api.tumblr.com/v2/tagged?api_key={0}&tag={1}'.format(api_key, query_string)

        nyt_api = NYTIMES_API_KEY
        nyt = "http://api.nytimes.com/svc/search/v1/article?format=json&query={0}&api-key=17d9623f92b7aab6e1430b41b1927462:14:67612802".format(query_string)

        pearson = "http://api.pearson.com/v2/dictionaries/entries?headword="+query_string+"&apikey="+ PEARSON_API_KEY

        print pearson
        resultP = simplejson.load(urllib.urlopen(pearson))

        try:
            definition = resultP['results'][0]['senses'][0]['definition']
        except:
            definition = "DNE"  #definition does not exist

        try:
            pos = resultP['results'][0]['part_of_speech']
        except:
            pos = ""

        n = []
        result1 = simplejson.load(urllib.urlopen(nyt))

        for p in result1['results']:
            try:
                title = p['title']
                author = p['byline']
                body = p['body']
                u = p['url']
                n.append({'title': title, 'author': author,
                          'body': body, 'url': u})
            except:
                pass

        t = []
        result2 = simplejson.load(urllib.urlopen(tumblr))
        for p in result2['response']:

            if ('photos' in p):
                x = p['photos']
                for item in x:
                    #imgpath = item['original_size']['url']
                    alt = item['alt_sizes']
                    thumbnail = alt[1]['url']  # len(alt)-3
                    t.append(thumbnail)

    context = {'query_string': query_string,
              'tumble': t,
              'nyt': n,
              'pos': pos,
              'definition': definition,
              'fonts': list(Style.objects.all())
              }

    return render_to_response('example/index.html', context,
                              context_instance=RequestContext(request))
