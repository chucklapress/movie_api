# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-28 18:37
from __future__ import unicode_literals

from django.db import migrations
import csv

class Migration(migrations.Migration):
    def datareview(apps, schema_editor):
        Rater = apps.get_model('app', 'Rater')
        Movie = apps.get_model('app', 'Movie')
        Review = apps.get_model('app', 'Review')
        with open('/Users/chucklapress/tiy-projects/movie_api/movieapi/movieapi/u.data', 'r') as inFile:
            data = csv.reader(inFile, delimiter='\t')
            for row in data:
                temp_rater = Rater.objects.get(id=row[0])
                temp_movie = Movie.objects.get(id=row[1])
                Review.objects.create(rater=temp_rater, movie=temp_movie, rating=row[2], timestamp=row[3])



    dependencies = [
        ('app', '0003_auto_20160628_1819'),
    ]

    operations = [
    migrations.RunPython(datareview)
    ]