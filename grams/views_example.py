from django.shortcuts import render_to_response, get_object_or_404
from instagram.client import InstagramAPI


def home(request):
    api = InstagramAPI(client_id='CLIENT_ID', client_secret='CLIENT_SECRET_KEY')

    #get popular images
    popular_media = api.media_popular(count=20)

    p = []
    for media in popular_media:
        print media.images['standard_resolution'].url
        p.append(media.images['standard_resolution'].url)

    return render_to_response("grams/index.html", {'popular': p})
