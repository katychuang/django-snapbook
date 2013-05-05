#django-snapbook

This django app takes photos from common social API's. It is still undergoing testing, check back for updates to this repository.


Setup
-----
To use this, first install the following

    $ pip install django, python-instagram, flickrapi, python-twitter

Sign up for the developer access keys at each website.

- Instagram [http://instagram.com/developer/clients/manage/]
- Tumblr [http://bestpracticesfororgs.tumblr.com/API]
- Pearson Dictionaries API [http://developer.pearson.com/apis]

More

- Wikipedia [http://www.mediawiki.org/wiki/API]
- Twitter [https://dev.twitter.com/]
- Flickr [http://www.flickr.com/services/api/]

Rename views_example.py to views.py and plop in your developer keys.

Usage
-----

Replace key strings with yours. Then use this bash prompt command to start server locally

    $ python manage.py runserver

SpeakerDeck for an overview of the structure:
https://speakerdeck.com/katychuang/nyc-pyladies-talk-5-dot-2-2013

#How might you use this app?
In essence, it's an educational tool. Here are some examples of usage:

##1. Style
A popular shoe style coming into trend is "wingtip" and often known as an oxford shoe. WIth the app, you can search for this term and see that it isn't an official word in a dictionary but people refer to this style, as shown by the images and the news articles.
<img src="https://lh3.googleusercontent.com/-CRsiKgsSFiQ/UYXCiqA0FII/AAAAAAAAINQ/Cm4_7HfymNs/w642-h547/styleA2.png" />

Similarly, the trend known as "french cuff" is coming into season. It typically refers to a type of sleeve cuff for mens dress shirt. But this term can also refer to extravagant choker necklaces.
<img src="https://lh5.googleusercontent.com/-GY6dRFBr1ww/UYXCi3QD4jI/AAAAAAAAINY/UQ8ZQLhQeKk/w642-h547/styleB2.png" />

Another style, shabby chic, is mainly a concept for interior decorating. It is something that people like to share pictures of as evidence by pictures of various parts of peoples homes, all with floral theme.
<img src="https://lh4.googleusercontent.com/-xqR7bnNjgAA/UYXCjSEZkjI/AAAAAAAAINU/WKkEFhm_K6k/w601-h547/styleC2.png" />

##2. Concepts
A picture dictionary can best be tested with a "concept" word that can connect with the viewer visually. You can see from the pictures that people consider bright colors as an aspect of euphoria. One person believes starbucks frappacino to be a euphoric.. potentially an angle of using a picture dictionary based on social API is to show marketing terms and colors that could be used in advertisements.
<img src="https://lh5.googleusercontent.com/-LYY_aItur6M/UYXChZRqndI/AAAAAAAAIMw/JTfzz7feenQ/w601-h547/conceptA2.png" />

##3. People
Some people receive a great deal of fame shortly after appearing on a reality tv show. This use case was to show how one such reality star is a recognizable entity on social media and a newspaper website. The dictionary does not yet recognize this person. The person's nick name brings out mostly opion articles.
<img src="https://lh3.googleusercontent.com/-Jx0y6DM4qLA/UYXCh38jUxI/AAAAAAAAINM/D7xPznNHMp4/w642-h547/personB2.png" />

There exists a famous rapper from NYC. The dictionary recognizes his name (though not part of speech), Tumblr users share flattering photos of this person, and the news paper has articles about this celebrity in connection with events cush as "Global Poverty Project benefit concert"
<img src="https://lh6.googleusercontent.com/-TQuh-fL2Iy8/UYXCnnI_-OI/AAAAAAAAINg/2mwkNnqqPV4/w631-h547/Screen+Shot+2013-05-04+at+10.22.45+PM.png" />

##4. Cats
Internet and cats are synonymous. This last usecase was to show the connection between "cat" images and news articles. Would the everyday tumblr user consider the concept the same as the official definition, and would that overlap with professional journalists' use of the terms? When a friend looked at the results he pointed out the article on bipolar disorder. His words, "I'm not surprised by this connection."
<img src="https://lh4.googleusercontent.com/-STCGHrY23_A/UYXChqFxa2I/AAAAAAAAINA/vlyV8XiKaPI/w642-h547/p2.png" />
