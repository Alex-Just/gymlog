from autoslug import AutoSlugField
from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..users.models import User


class Program(models.Model):
    owner = models.ForeignKey(User, related_name='programs')
    title = models.CharField(_('title'), max_length=100)

    # `always_update` is intended; although, "cool URIs don’t change" (http://w3.org/Provider/Style/URI.html)
    slug = AutoSlugField(populate_from='title', unique_with=['owner'], always_update=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('program')
        verbose_name_plural = _('programs')

        unique_together = (
            ('owner', 'title'),
        )


class Day(models.Model):
    program = models.ForeignKey(Program, related_name='days')

    ind = models.PositiveSmallIntegerField(_('order'))
    title = models.CharField(_('title'), max_length=50)

    # `always_update` is intended; although, "cool URIs don’t change" (http://w3.org/Provider/Style/URI.html)
    slug = AutoSlugField(populate_from='title', unique_with=['program'], always_update=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('ind',)
        verbose_name = _('day')
        verbose_name_plural = _('days')

        unique_together = (
            ('program', 'ind'),
            ('program', 'title'),
        )


class Exercise(models.Model):
    day = models.ForeignKey(Day, related_name='exercises')

    ind = models.PositiveSmallIntegerField(_('order'))
    title = models.CharField(_('title'), max_length=100)
    note = models.TextField(_('note'), blank=True, default='')
    video = models.URLField(_('video'), blank=True, default='')

    # `always_update` is intended; although, "cool URIs don’t change" (http://w3.org/Provider/Style/URI.html)
    slug = AutoSlugField(populate_from='title', unique_with=['day'], always_update=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('ind',)
        verbose_name = _('exercise')
        verbose_name_plural = _('exercises')

        unique_together = (
            ('day', 'ind'),
            ('day', 'title'),
        )


class Set(models.Model):
    exercise = models.ForeignKey(Exercise, related_name='sets')

    ind = models.PositiveSmallIntegerField(_('order'))
    reps = models.PositiveSmallIntegerField(_('reps'), null=True, blank=True)
    weight = models.FloatField(_('weight'), null=True, blank=True)

    class Meta:
        ordering = ('ind',)
        verbose_name = _('set')
        verbose_name_plural = _('sets')

        unique_together = (
            ('exercise', 'ind'),
        )
