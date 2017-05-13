from django.contrib import admin

from .models import Program, Day, Exercise, Set, DayExercise


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
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(DayExercise)
class DayExerciseAdmin(admin.ModelAdmin):
    def get_owner(self, obj):
        return obj.day.program.owner

    get_owner.short_description = 'Owner'

    def get_program(self, obj):
        return obj.day.program

    get_program.short_description = 'Program'

    def get_exercise(self, obj):
        return obj.exercise

    get_exercise.short_description = 'Exercise'

    list_display = ('slug', 'ind', 'day', 'get_exercise', 'get_program', 'get_owner')
    search_fields = ('day', 'program', 'owner__username')


@admin.register(Set)
class SetAdmin(admin.ModelAdmin):
    def get_owner(self, obj):
        return obj.day_exercise.day.program.owner

    get_owner.short_description = 'Owner'

    def get_program(self, obj):
        return obj.day_exercise.day.program

    get_program.short_description = 'Program'

    def get_day(self, obj):
        return obj.day_exercise.day

    get_day.short_description = 'Day'

    list_display = ('ind', 'reps', 'weight', 'day_exercise', 'get_day', 'get_program', 'get_owner')
    search_fields = ('day', 'program', 'owner__username')
