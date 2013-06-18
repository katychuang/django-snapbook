from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'example.views.home'),  # home page
                       url(r'^flickr/$', 'example.views.flickr'),  # Flickr
                       url(r'^instagram/$', 'example.views.grams'),  # Instagram
                       url(r'^tumblr/$', 'example.views.tumblr'),  # Tumblr
                       url(r'^twitter/$', 'example.views.tweets'),  # Twitter
                       url(r'^search/$', 'example.views.search'),

                       # Examples:
                       # url(r'^snapbook/', include('snapbook.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
                       )
