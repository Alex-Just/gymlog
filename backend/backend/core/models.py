from autoslug import AutoSlugField
from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..users.models import User


class Program(models.Model):
    owner = models.ForeignKey(User, related_name='programs', verbose_name=_('owner'))
    title = models.CharField(_('title'), max_length=100)

    # `always_update` is intended; although, "cool URIs don’t change" (http://w3.org/Provider/Style/URI.html)
    slug = AutoSlugField(populate_from='title', unique_with=['owner'], always_update=True, verbose_name=_('slug'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('program')
        verbose_name_plural = _('programs')

        unique_together = (
            ('owner', 'title'),
        )


class Day(models.Model):
    program = models.ForeignKey(Program, related_name='days', verbose_name=_('program'))

    ind = models.PositiveSmallIntegerField(_('order'))
    title = models.CharField(_('title'), max_length=50)

    # `always_update` is intended; although, "cool URIs don’t change" (http://w3.org/Provider/Style/URI.html)
    slug = AutoSlugField(populate_from='title', unique_with=['program'], always_update=True, verbose_name=_('slug'))

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
    title = models.CharField(_('title'), max_length=100, unique=True)
    note = models.TextField(_('note'), blank=True, default='')
    video = models.URLField(_('video'), blank=True, default='')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('exercise')
        verbose_name_plural = _('exercises')


class DayExercise(models.Model):
    day = models.ForeignKey(Day, related_name='exercises', verbose_name=_('day'))

    ind = models.PositiveSmallIntegerField(_('order'))
    exercise = models.ForeignKey(Exercise, related_name='day_exercises', verbose_name=_('exercise'))

    # `always_update` is intended; although, "cool URIs don’t change" (http://w3.org/Provider/Style/URI.html)
    slug = AutoSlugField(populate_from='_get_slug', unique_with=['day'], always_update=True, verbose_name=_('slug'))

    def _get_slug(self):
        return self.exercise.title

    def __str__(self):
        return 'Program: {}, Day: #{} {}, Exercise: #{} {}' \
            .format(self.day.program.title, self.day.ind, self.day.title, self.ind, self.exercise.title)

    class Meta:
        ordering = ('day__ind', 'ind')
        verbose_name = _('day exercise')
        verbose_name_plural = _('day exercises')

        unique_together = (
            ('day', 'ind'),
            ('day', 'exercise'),
        )


class Set(models.Model):
    day_exercise = models.ForeignKey(DayExercise, related_name='sets', verbose_name=_('day exercise'))

    ind = models.PositiveSmallIntegerField(_('order'))
    reps = models.PositiveSmallIntegerField(_('reps'), null=True, blank=True)
    weight = models.FloatField(_('weight'), null=True, blank=True)

    class Meta:
        ordering = ('day_exercise__day__ind', 'day_exercise__ind', 'ind')
        verbose_name = _('set')
        verbose_name_plural = _('sets')

        unique_together = (
            ('day_exercise', 'ind'),
        )
