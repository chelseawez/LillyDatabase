from db_lilly.models import Media, LoanInfo, Item, AKA, Production, Summary, Actor, Director, Genre, TVSeason, Language, Poster
from django.contrib import admin

admin.site.register(Media)
admin.site.register(LoanInfo)
admin.site.register(Item)
admin.site.register(AKA)
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Production)
admin.site.register(Summary)
admin.site.register(TVSeason)
admin.site.register(Language)
admin.site.register(Poster)
