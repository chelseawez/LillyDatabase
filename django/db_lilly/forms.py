from django import forms
from db_lilly.models import AKA, Actor, Production, Summary, Director, Genre, Item, Media, LoanInfo, TVSeason, Language

class SearchForm(forms.Form):
    blank = [("", "All")]
    genre_choices = blank + [(genre, str(genre)) for genre in Genre.objects.order_by('genre').values_list('genre', flat=True).distinct()]
    form_choices = blank + [(form, str(form)) for form in Media.objects.order_by('format').values_list('format', flat=True).distinct()]
    fortv_choices = blank + [(filmortv, str(filmortv)) for filmortv in Media.objects.order_by('film_or_tv').values_list('film_or_tv', flat=True).distinct()]
    rate_choices = blank + [(rating, str(rating)) for rating in Media.objects.order_by('rating').values_list('rating', flat=True).distinct()]
#    lang_choices = blank + [(lang, str(lang)) for lang in Language.objects.order_by('language').values_list('language',flat=True).distinct()]
    country_choices = blank + [(country, str(country)) for country in Media.objects.order_by('country').values_list('country', flat=True).distinct()]
#    loan_type_choices = blank + [(loan_type, str(loan_type)) for loan_type in LoanInfo.objects.order_by('loan_type').values_list('loan_type', flat=True).distinct()]
#    location_choices = blank + [(location, str(location)) for location in LoanInfo.objects.order_by('location').values_list('location', flat=True).distinct()]
    avail_choices = blank + [(avail, str(avail)) for avail in Item.objects.order_by('availability').values_list('availability', flat=True).distinct()]

    title_keyword = forms.CharField(required=False)
    genre = forms.ChoiceField(choices=genre_choices, required=False)
    film_or_TV = forms.ChoiceField(choices=fortv_choices, required=False)
    format = forms.ChoiceField(choices=form_choices, required=False)
    rating = forms.ChoiceField(choices=rate_choices, required=False)
    earliest_release_year = forms.IntegerField(required=False, help_text="(To search all filmed resources released through a given year, leave blank and fill the next field.)")
    latest_release_year = forms.IntegerField(required=False, help_text="(To search all filmed resources released in a given year through the present year, leave blank and fill the previous field.)")
#    language = forms.ChoiceField(choices=lang_choices, required=False)    --> could not include because of encoding issues; plan to include in future
    country = forms.ChoiceField(choices=country_choices, required=False)
#    loan_type = forms.ChoiceField(choices=loan_type_choices, required=False)
    availability = forms.ChoiceField(choices=avail_choices, required=False)
#    location = forms.ChoiceField(choices=location_choices, required=False)    

