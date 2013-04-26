from django.shortcuts import render_to_response, get_object_or_404
from instagram.client import InstagramAPI
import twitter


def grams(request):
    api = InstagramAPI(client_id='d60340d55d864859a9d3a34f50a6d816',
                       client_secret='89d0d579e9714a9780c4352aa3872968')

    #get popular images
    popular_media = api.media_popular(count=20)

    #add popular images
    p = []
    for media in popular_media:
        print media.images['standard_resolution'].url
        p.append(media.images['standard_resolution'].url)

    #pass to template
    return render_to_response("example/index.html", {'popular': p})


def tweets(request):
    api = twitter.Api(consumer_key='consumer_key',
                      consumer_secret='consumer_secret',
                      access_token_key='access_token',
                      access_token_secret='access_token_secret')
    print api.VerifyCredentials()
