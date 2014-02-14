from django.conf.urls import patterns, include, url

urlpatterns = patterns('db_lilly.views',
    url(r'^$', 'home'),
    url(r'^library-info$', 'library_info'),
    url(r'^all-dvds$', 'all_dvds', name='all_dvds'),

    url(r'^film$', 'all_films'),
    url(r'^film/(?P<mediaid>[^/]+)$', 'film'),

    url(r'^tv$', 'all_tv'),
    url(r'^tv/(?P<mediaid>[^/]+)$', 'tv'),

    url(r'^genre$', 'all_genres'),
    url(r'^genre/(?P<genre_name>[^/]+)$', 'genre'),

    url(r'^devil-dvds$', 'devil_dvds'),

    url(r'^people$', 'all_people'),
    url(r'^people/(?P<name>[^/]+)$', 'people'),

    url(r'^company$', 'all_companies'),
    url(r'^company/(?P<company_name>[^/]+)$', 'company'),

    url(r'^login$', 'login'),
    url(r'^logout$', 'logout'),
    
    url(r'^results$', 'getResultForm')
    )
