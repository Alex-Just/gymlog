# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-13 11:27
from __future__ import unicode_literals

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ind', models.PositiveSmallIntegerField(verbose_name='order')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='title', unique_with=['program'], verbose_name='slug')),
            ],
            options={
                'verbose_name': 'day',
                'verbose_name_plural': 'days',
                'ordering': ('ind',),
            },
        ),
        migrations.CreateModel(
            name='DayExercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ind', models.PositiveSmallIntegerField(verbose_name='order')),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='_get_slug', unique_with=['day'], verbose_name='slug')),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercises', to='core.Day', verbose_name='day')),
            ],
            options={
                'verbose_name': 'day exercise',
                'verbose_name_plural': 'day exercises',
                'ordering': ('day__ind', 'ind'),
            },
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='title')),
                ('note', models.TextField(blank=True, default='', verbose_name='note')),
                ('video', models.URLField(blank=True, default='', verbose_name='video')),
            ],
            options={
                'verbose_name': 'exercise',
                'verbose_name_plural': 'exercises',
            },
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='title', unique_with=['owner'], verbose_name='slug')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='programs', to=settings.AUTH_USER_MODEL, verbose_name='owner')),
            ],
            options={
                'verbose_name': 'program',
                'verbose_name_plural': 'programs',
            },
        ),
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ind', models.PositiveSmallIntegerField(verbose_name='order')),
                ('reps', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='reps')),
                ('weight', models.FloatField(blank=True, null=True, verbose_name='weight')),
                ('day_exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sets', to='core.DayExercise', verbose_name='day exercise')),
            ],
            options={
                'verbose_name': 'set',
                'verbose_name_plural': 'sets',
                'ordering': ('day_exercise__day__ind', 'day_exercise__ind', 'ind'),
            },
        ),
        migrations.AddField(
            model_name='dayexercise',
            name='exercise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='day_exercises', to='core.Exercise', verbose_name='exercise'),
        ),
        migrations.AddField(
            model_name='day',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='days', to='core.Program', verbose_name='program'),
        ),
        migrations.AlterUniqueTogether(
            name='set',
            unique_together=set([('day_exercise', 'ind')]),
        ),
        migrations.AlterUniqueTogether(
            name='program',
            unique_together=set([('owner', 'title')]),
        ),
        migrations.AlterUniqueTogether(
            name='dayexercise',
            unique_together=set([('day', 'exercise'), ('day', 'ind')]),
        ),
        migrations.AlterUniqueTogether(
            name='day',
            unique_together=set([('program', 'title'), ('program', 'ind')]),
        ),
    ]
