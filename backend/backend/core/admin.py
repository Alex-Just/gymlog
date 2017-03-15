# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import admin

from .models import Program, Day, Exercise, Set


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'owner')
    search_fields = ('title', 'owner__username')


@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    def get_owner(self, obj):
        return obj.program.owner

    get_owner.short_description = 'Owner'

    list_display = ('title', 'slug', 'ind', 'program', 'get_owner')
    search_fields = ('title', 'program', 'owner__username')


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    def get_owner(self, obj):
        return obj.day.program.owner

    get_owner.short_description = 'Owner'

    def get_program(self, obj):
        return obj.day.program

    get_program.short_description = 'Program'

    list_display = ('title', 'slug', 'ind', 'day', 'get_program', 'get_owner')
    search_fields = ('title', 'day', 'program', 'owner__username')


@admin.register(Set)
class SetAdmin(admin.ModelAdmin):
    def get_owner(self, obj):
        return obj.exercise.day.program.owner

    get_owner.short_description = 'Owner'

    def get_program(self, obj):
        return obj.exercise.day.program

    get_program.short_description = 'Program'

    def get_day(self, obj):
        return obj.exercise.day

    get_day.short_description = 'Day'

    list_display = ('ind', 'exercise', 'get_day', 'get_program', 'get_owner')
    search_fields = ('day', 'program', 'owner__username')
