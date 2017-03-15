from django.contrib.admin.sites import AdminSite
from test_plus.test import TestCase

from ..admin import DayAdmin, ExerciseAdmin, SetAdmin
from ..models import Day, Program, Exercise, Set


class TestDayAdmin(TestCase):
    def setUp(self):
        self.day_admin = DayAdmin(Day, AdminSite())
        self.user = self.make_user()
        self.program_title = 'My program'
        self.day_title = 'First day 💪'
        self.program = Program.objects.create(owner=self.user, title=self.program_title)
        self.day = Day.objects.create(program=self.program, title=self.day_title, ind=1)

    def test_get_owner(self):
        self.assertEqual(self.day_admin.get_owner(self.day), self.user)


class TestExerciseAdmin(TestCase):
    def setUp(self):
        self.exercise_admin = ExerciseAdmin(Exercise, AdminSite())
        self.user = self.make_user()
        self.program_title = 'My program'
        self.day_title = 'First day 💪'
        self.exercise_title = 'First exercise 💪'
        self.program = Program.objects.create(owner=self.user, title=self.program_title)
        self.day = Day.objects.create(program=self.program, title=self.day_title, ind=1)
        self.exercise = Exercise.objects.create(day=self.day, title=self.exercise_title, ind=1)

    def test_get_owner(self):
        self.assertEqual(self.exercise_admin.get_owner(self.exercise), self.user)

    def test_get_program(self):
        self.assertEqual(self.exercise_admin.get_program(self.exercise), self.program)


class TestSetAdmin(TestCase):
    def setUp(self):
        self.set_admin = SetAdmin(Set, AdminSite())
        self.user = self.make_user()
        self.program_title = 'My program'
        self.day_title = 'First day 💪'
        self.exercise_title = 'First exercise 💪'
        self.program = Program.objects.create(owner=self.user, title=self.program_title)
        self.day = Day.objects.create(program=self.program, title=self.day_title, ind=1)
        self.exercise = Exercise.objects.create(day=self.day, title=self.exercise_title, ind=1)
        self.set = Set.objects.create(exercise=self.exercise, ind=1)

    def test_get_owner(self):
        self.assertEqual(self.set_admin.get_owner(self.set), self.user)

    def test_get_program(self):
        self.assertEqual(self.set_admin.get_program(self.set), self.program)

    def test_get_day(self):
        self.assertEqual(self.set_admin.get_day(self.set), self.day)
