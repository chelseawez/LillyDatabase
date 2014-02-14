# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

# import django_tables2 as tables
from django.db import models 

class Media(models.Model):
    mediaid = models.CharField(max_length=20, primary_key=True)
    primary_title = models.CharField(max_length=200)
    release_year = models.IntegerField()
    country = models.CharField(max_length=45)
    format = models.CharField(max_length=20)
    film_or_tv = models.CharField(max_length=10)
    title_sort = models.CharField(max_length=200)
    rating = models.CharField(max_length=20)
    tmdb_id = models.CharField(max_length=20)
    tagline = models.CharField(max_length=400)
    flag = models.CharField(max_length=20)
    class Meta:
        db_table = 'media'
        ordering = ['title_sort']
    def __unicode__(self):
        return self.primary_title

#class MediaTable(tables.Table):
#    title = tables.Column(name="Title")
#    year = tables.Column(name="Year")
#    country = tables.Column(name="Country")
#    class Meta:
#        model = Media

class LoanInfo(models.Model):
    loanid = models.CharField(max_length=10, primary_key=True)
    loan_type = models.CharField(max_length=30)
    loan_time = models.CharField(max_length=10)
    location = models.CharField(max_length=20)
    class Meta:
        db_table = 'loaninfo'
    def __unicode__(self):
        return self.loan_type

class Item(models.Model):
    itemid = models.CharField(max_length=20, primary_key=True)
    mediaid = models.ForeignKey(Media, db_column='mediaid')
    call_number = models.CharField(max_length=65)
    loanid = models.ForeignKey(LoanInfo, db_column='loanid')
    availability = models.CharField(max_length=25)
    current = models.BooleanField()
    class Meta:
        db_table = 'item'
    def __unicode__(self):
        return u'%s, %s' % (self.mediaid, self.pk)

class Summary(models.Model):
    mediaid = models.ForeignKey(Media, db_column='mediaid', primary_key=True)
    summary = models.CharField(max_length=1600)
    class Meta:
        db_table = 'summary'
    def __unicode__(self):
        return self.pk

class Poster(models.Model):
    mediaid = models.ForeignKey(Media, db_column='mediaid', primary_key=True)
    poster = models.CharField(max_length=100)
    class Meta:
        db_table = 'poster'
    def __unicode__(self):
        return self.pk

class Actor(models.Model):
    actor_id = models.IntegerField(primary_key=True)
    mediaid = models.ForeignKey(Media, db_column='mediaid', db_index=True)
    performer = models.CharField(max_length=50, db_index=True)
    class Meta:
        db_table = 'actor'
    def __unicode__(self):
	return u'%s, %s' % (self.performer, self.mediaid)

class AKA(models.Model):
    AKA_id = models.IntegerField(primary_key=True)
    mediaid = models.ForeignKey(Media, db_column='mediaid', db_index=True)
    secondary_title = models.CharField(max_length=250)
    class Meta:
        db_table = 'aka'
    def __unicode__(self):
	return u'%s, %s' % (self.secondary_title, self.mediaid)

class Director(models.Model):
    director_id = models.IntegerField(primary_key=True)
    mediaid = models.ForeignKey(Media, db_column='mediaid', db_index=True)
    director = models.CharField(max_length=40, db_index=True)
    class Meta:
        db_table = 'director'
    def __unicode__(self):
	return u'%s, %s' % (self.director, self.mediaid)

class Genre(models.Model):
    genre_id = models.IntegerField(primary_key=True)
    mediaid = models.ForeignKey(Media, db_column='mediaid', db_index=True)
    genre = models.CharField(max_length=20, db_index=True)
    class Meta:
        db_table = 'genre'
        ordering = ['mediaid']
    def __unicode__(self):
	return u'%s, %s' % (self.genre, self.mediaid)

class Production(models.Model):
    production_id = models.IntegerField(primary_key=True)
    mediaid = models.ForeignKey(Media, db_column='mediaid')
    company = models.CharField(max_length=100)
    match = models.CharField(max_length=100, db_index=True)
    class Meta:
        db_table = 'production'
    def __unicode__(self):
        return u'%s, %s' % (self.mediaid, self.match)

class TVSeason(models.Model):
    mediaid = models.ForeignKey(Media, primary_key=True, db_column='mediaid', related_name='tvseason_mediaid')
    season = models.IntegerField()
    class Meta:
        db_table = 'tvseason'
    def __unicode__(self):
        return self.pk

class Language(models.Model):
    language_id = models.IntegerField(primary_key=True)
    mediaid = models.ForeignKey(Media, db_column='mediaid', db_index=True)
    language = models.CharField(max_length=50, db_index=True)
    class Meta:
        db_table = 'language'
    def __unicode__(self):
        return u'%s, %s' % (self.mediaid, self.language)
