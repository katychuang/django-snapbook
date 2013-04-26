from django.shortcuts import render_to_response, get_object_or_404
from instagram.client import InstagramAPI
import twitter, flickrapi


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
