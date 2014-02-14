import re, operator
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse, reverse_lazy
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404, render
from db_lilly.models import AKA, Actor, Production, Summary, Director, Genre, Item, LoanInfo, Media, TVSeason, Language, Poster
from django.forms.models import ModelForm, inlineformset_factory
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from db_lilly.forms import SearchForm
from django.views.generic.edit import FormView
from django.db.models import Q
import operator

def home(request):
    return render_to_response('db_lilly/home.html',
        {},
        context_instance=RequestContext(request))

def all_dvds(request):
    return render_to_response('db_lilly/all-dvds.html',
        { 'dvds' : Media.objects.all().distinct('title_sort') },
        context_instance=RequestContext(request))

def all_tv(request):
    media = Media.objects.filter(film_or_tv="TV")
    return render_to_response('db_lilly/all-tv.html',
        { 'tv_shows' : media.distinct('title_sort') 
#          'table' : MediaTable(media)
        },
        context_instance=RequestContext(request))

def tv(request, mediaid):
    media_table = get_object_or_404(Media, pk=mediaid, film_or_tv="TV")

    try:
        summary = Summary.objects.get(pk=mediaid)
    except Summary.DoesNotExist:
        summary = None
    try:
        poster = Poster.objects.get(pk=mediaid)
    except:
        poster = None

    return render_to_response('db_lilly/tv.html',
        { 'media' : media_table,
          'title' : media_table.primary_title,
          'genres' : media_table.genre_set.all(),
          'actors' : media_table.actor_set.all(),
          'directors' : media_table.director_set.all(),
          'items' : media_table.item_set.all().order_by('call_number'),
          'language' : media_table.language_set.all(),
          'summary' : summary,
          'companies' : media_table.production_set.all(),
          'poster' : poster,
          'season' : TVSeason.objects.get(pk=mediaid),
        },
        context_instance=RequestContext(request))

def all_films(request):
    return render_to_response('db_lilly/all-films.html',
        { 'films' : Media.objects.filter(film_or_tv__exact="Film").order_by('title_sort').distinct('title_sort') },
        context_instance=RequestContext(request))

def film(request, mediaid):
    media_table = get_object_or_404(Media, pk=mediaid, film_or_tv="Film")
    try:
        summary = Summary.objects.get(pk=mediaid)
    except Summary.DoesNotExist:
        summary = None
    try:
        poster = Poster.objects.get(pk=mediaid)
    except:
        poster = None
    return render_to_response('db_lilly/film.html',
        { 'media' : media_table,
          'title' : media_table.primary_title,
          'genres' : media_table.genre_set.all(),
          'actors' : media_table.actor_set.all(),
          'directors' : media_table.director_set.all(),
          'items' : media_table.item_set.all().order_by('call_number'),
          'language' : media_table.language_set.all(),
          'summary' : summary,
          'companies' : media_table.production_set.all(),
          'poster' : poster,
        },
        context_instance=RequestContext(request))

def all_genres(request):
    return render_to_response('db_lilly/all-genres.html',
        { 'distinct_genres' : Genre.objects.order_by('genre').values_list('genre', flat=True).distinct(),
        },
        context_instance=RequestContext(request))

def genre(request, genre_name):
    this_genre = get_list_or_404(Genre, genre=genre_name)
    return render_to_response('db_lilly/genre.html',
        { 'name' : genre_name,
          'genre' : this_genre,
        },
        context_instance=RequestContext(request))

def all_companies(request):
    return render_to_response('db_lilly/all-companies.html',
        { 'distinct_companies' : Production.objects.order_by('match').values_list('match', flat=True).distinct(),
        },
        context_instance=RequestContext(request))

def company(request, company_name):
    this_company = get_list_or_404(Production, match=company_name)
    return render_to_response('db_lilly/company.html',
        { 'name' : company_name,
          'company' : this_company,
        },
        context_instance=RequestContext(request))

def all_people(request):
    people = list(Actor.objects.values_list('performer', flat=True).distinct())
    directors = list(Director.objects.values_list('director', flat=True).distinct())
    for director in directors:
       if director not in people:
          people.append(director)
    people.sort()
    return render_to_response('db_lilly/all-people.html',
        { 'people' : people
        },
        context_instance=RequestContext(request))

def people(request, name):
    actor_list = list(Actor.objects.filter(performer=name))
    director_list = list(Director.objects.filter(director=name))
    if (not actor_list) and (not director_list):
        raise Http404
    return render_to_response('db_lilly/people.html',
        { 'actor' : actor_list,
          'director' : director_list,
          'person' : name,
        },
        context_instance=RequestContext(request))

def devil_dvds(request):
    items = Item.objects.filter(loanid="PLV8")
    media = Media.objects.filter(mediaid__in=list(items.values_list('mediaid', flat=True).distinct()))
    posters = Poster.objects.filter(mediaid__in=list(items.values_list('mediaid', flat=True).distinct()))
    return render_to_response('db_lilly/devil-dvds.html',
        { 'dvds' : media,
          'posters' : posters,
        },
        context_instance=RequestContext(request))

def library_info(request):
    return render_to_response('db_lilly/library-info.html',
        {},
        context_instance=RequestContext(request))

def login(request):
    return render_to_response('db_lilly/login.html',
        {},
        context_instance=RequestContext(request))

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('db_lilly.views.home'))

def getResultForm(request):
    form = SearchForm()
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
	    title_keyword = form.cleaned_data['title_keyword']
            title_keywords = title_keyword.split(",") 
            selected_genre = form.cleaned_data['genre']
            selected_film_or_tv = form.cleaned_data['film_or_TV']
            selected_format = form.cleaned_data['format']
	    selected_rating = form.cleaned_data['rating']
	    selected_earliest_year = form.cleaned_data['earliest_release_year']
	    selected_latest_year = form.cleaned_data['latest_release_year']
	    selected_country = form.cleaned_data['country']
#            selected_lang = form.cleaned_data['language']
	    selected_avail = form.cleaned_data['availability']
#	    selected_loan_type = form.cleaned_data['loan_type']

	    #set media to all objects
	    media = Media.objects.all()

            #filter with simple selections
            if selected_rating != "":
                media = media.filter(rating=selected_rating)

	    if selected_format != "":
		media = media.filter(format=selected_format)

	    if selected_film_or_tv != "":
		media = media.filter(film_or_tv=selected_film_or_tv)

	    if (selected_earliest_year is not None) and (selected_latest_year is not None) and (selected_latest_year >= selected_earliest_year):
		media = media.filter(release_year__gte= selected_earliest_year, release_year__lte=selected_latest_year)
	    elif (selected_earliest_year is None) and (selected_latest_year is not None):
		media = media.filter(release_year__lte=selected_latest_year)
	    elif (selected_earliest_year is not None) and (selected_latest_year is None):
		media = media.filter(release_year__gte=selected_earliest_year)

	    if selected_country != "":
		media = media.filter(country=selected_country)

	    #filters that involve joins (keywords will eventually involve AKA table)
            if len(title_keywords) > 0:
                title_keywords = title_keyword.split(",")
                media = media.filter(reduce(operator.and_, (Q(primary_title__icontains=x) for x in title_keywords)))

            if selected_genre != "":
                this_genre = Genre.objects.filter(genre=selected_genre).values_list('mediaid',flat=True)
                media = media.filter(mediaid__in=this_genre)

            if selected_avail != "":
                this_avail = Item.objects.filter(availability=selected_avail).values_list('mediaid',flat=True)
                media = media.filter(mediaid__in=this_avail)

	    #couldn't include for time being b/c of encoding issues
#            if selected_lang != "":
#                this_lang = Language.objects.filter(language=selected_lang)
#                media = media.filter(mediaid__in=this_lang)

            return render_to_response('db_lilly/results.html',
                {'results': media.order_by('title_sort').distinct('title_sort'),
                 'form': form},
                context_instance=RequestContext(request))

    return render_to_response('db_lilly/search.html',
        { 'form' : SearchForm() },
        context_instance=RequestContext(request))

class PartialFilmForm(ModelForm):
    class Meta:
        model = Media
        # Leave out name so it cannot be edited; at the same time, it means that
        # it won't be in the data submitted through the form either:
        exclude = ('primary_title',)
