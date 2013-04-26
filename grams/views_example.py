from django.shortcuts import render_to_response, get_object_or_404
from instagram.client import InstagramAPI


def home(request):
    # access_token = ""
    # api = InstagramAPI(access_token=access_token)
    # recent_media, next = instagram_client.user_recent_media(user_id=user.instagram_userid, count=count)
    # for media in recent_media:
    #     print media.caption.text

    api = InstagramAPI(client_id='CLIENT_ID', client_secret='CLIENT_SECRET_KEY')

    #get popular images
    popular_media = api.media_popular(count=20)

    p = []
    for media in popular_media:
        print media.images['standard_resolution'].url
        p.append(media.images['standard_resolution'].url)

    return render_to_response("grams/index.html", {'popular': p})


    # Subscribe to all media tagged with 'warbyparker'
    # api.create_subscription(object='tag', object_id='warbyparker', aspect='media', callback_url='http://localhost:8000/hook/instagram')
