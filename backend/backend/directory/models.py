from django.db import models


class Exercise(models.Model):
    title = models.CharField(_('title'), max_length=100, unique=True)
    note = models.TextField(_('note'), blank=True, default='')
    video = models.URLField(_('video'), blank=True, default='')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('exercise')
        verbose_name_plural = _('exercises')
