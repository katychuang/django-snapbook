from django.shortcuts import render_to_response, get_object_or_404
from instagram.client import InstagramAPI
# import twitter, tweetstream
import tweepy, simplejson, urllib
import flickrapi
#import img_downloader, image_list


def home(request):
    return render_to_response("example/index.html", {'page_title': 'django-snapbook', 'name': 'home'})


def flickr(request):
    api_key = 'ee91a3c21445b9f06b15d26f977dbde3'
    api_secret = '884bf333ad3b377b'

    flickr = flickrapi.FlickrAPI(api_key, api_secret, format='json')
    photos = flickr.photos_search(user_id='73509078@N00', per_page='10')
    sets = flickr.photosets_getList(user_id='73509078@N00')

    # group_id=826069%40N20

    # result = simplejson.load(urllib.urlopen(url))
    # #print result['photos']
    # #pprint(result['photos']['photo'])

    # for item in result['photos']['photo']:
    #     src = "http://farm{0}.staticflickr.com/{1}/{2}_{3}.jpg".format(item['farm'], item['server'], item['id'], item['secret'])
    #     imgpath = "<div class=\"slide\"><img src=\"" + src + "\"></div>"
    #     print imgpath

    return render_to_response("example/index.html", {'twitters': sets,
        'page_title': 'Photos from Flickr'})




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
    return render_to_response("example/index.html", {'popular': p, 'page_title': 'Photos from Instagram'})


def tumblr(request):
    tag = "fashion"
    api_key = "6X5uXLI78DNVdntorxVJ0r2LHsMYAxva9Vf3NaV9diua1K5SIB"
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
                              {'popular': t, 'page_title': 'Photos from tumblr'}
                              )


def tweets(request):
    consumer_key = '4YeMHSvzkJr9fCen8fNqw'
    consumer_secret = 'V0J6uQMPYdYjHCCn08K2qoZHVDS1838oMu4DH7wX2Fo'
    key = '17883224-ZUck4M4i0RtgM3RbCgNPS6sTQvL9ryIL0a5Us00Bv'
    secret = '982gQiVr0QtjSBGHnho8b13RUpNo5TazUO5AHgzR30'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(key, secret)
    api = tweepy.API(auth)
    #public_tweets = tweepy.api.public_timeline()

    # for tweet in public_tweets:
    #     print tweet.text

    # seeds = ["#fashion", "fashion"]
    t = []

    # with tweetstream.FilterStream("poesypoesy", "syllablizer", track=seeds) as stream:
    #         for tweet in stream:
    #             urls = [url for url in tweet['text'].split() if 'http://t.co' in url]
    #             if len(urls) > 0:

    #                 print 'URLs'
    #                 print urls

    #                 for url in urls:
    #                     #generate list of images in page
    #                     img_list = image_list.get_img_list(url)

    #                     #get images
    #                     for img_url in img_list:
    #                         #img_downloader.getImg(img_url)
    #                         t.append(img_url)


    # api = twitter.Api(consumer_key='4YeMHSvzkJr9fCen8fNqw',
    #                   consumer_secret='V0J6uQMPYdYjHCCn08K2qoZHVDS1838oMu4DH7wX2Fo',
    #                   access_token_key='17883224-ZUck4M4i0RtgM3RbCgNPS6sTQvL9ryIL0a5Us00Bv',
    #                   access_token_secret='982gQiVr0QtjSBGHnho8b13RUpNo5TazUO5AHgzR30')
    # #print api.VerifyCredentials()
    # t = twitter.Trend(query='fashion')


    return render_to_response("example/index.html",
                              {'twitters': t,
                               'page_title': 'Photos from twitter'})
