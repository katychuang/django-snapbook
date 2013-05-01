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
