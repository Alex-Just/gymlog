from django.db import transaction, IntegrityError
from test_plus.test import TestCase

from ..models import Program, Day, Exercise, Set


class TestProgram(TestCase):
    def setUp(self):
        self.user = self.make_user()
        self.user2 = self.make_user('testuser2')
        self.program_title = 'My program 💪'
        self.program = Program.objects.create(owner=self.user, title=self.program_title)

    def test_owner(self):
        self.assertEqual(
            self.program.owner.username,
            'testuser'  # This is the default username for self.make_user()
        )

    def test__str__(self):
        self.assertEqual(
            self.program.__str__(),
            self.program_title
        )

    def test_slug(self):
        self.assertEqual(
            self.program.slug,
            'My-program'
        )

    def test_title_duplicate(self):
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                Program.objects.create(owner=self.user, title=self.program_title)

    def test_title_no_duplicates_between_users(self):
        Program.objects.create(owner=self.user2, title=self.program_title)

        # def test_get_absolute_url(self):
        #     self.assertEqual(
        #         self.program.get_absolute_url(),
        #         '/programs/my-program/'
        #     )


class TestDay(TestCase):
    def setUp(self):
        self.user = self.make_user()
        self.user2 = self.make_user('testuser2')
        self.program_title = 'My program'
        self.day_title = 'First day 💪'
        self.program = Program.objects.create(owner=self.user, title=self.program_title)
        self.not_my_program = Program.objects.create(owner=self.user2, title=self.program_title)
        self.day = Day.objects.create(program=self.program, title=self.day_title, ind=1)

    def test_owner(self):
        self.assertEqual(
            self.day.program.owner.username,
            'testuser'  # This is the default username for self.make_user()
        )

    def test__str__(self):
        self.assertEqual(
            self.day.__str__(),
            self.day_title
        )

    def test_slug(self):
        self.assertEqual(
            self.day.slug,
            'First-day'
        )

    def test_ind_null(self):
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                Day.objects.create(program=self.program, title=self.day_title)

    def test_ind_duplicate(self):
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                Day.objects.create(program=self.program, title=self.day_title + '2', ind=1)

    def test_ind_no_duplicates_between_users(self):
        Day.objects.create(program=self.not_my_program, title=self.day_title, ind=1)

    def test_title_null(self):
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                Day.objects.create(program=self.program, ind=1)

    def test_title_duplicate(self):
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                Day.objects.create(program=self.program, title=self.day_title, ind=2)

                # def test_get_absolute_url(self):
                #     self.assertEqual(
                #         self.program.get_absolute_url(),
                #         '/programs/my-program/'
                #     )


class TestExercise(TestCase):
    def setUp(self):
        self.user = self.make_user()
        self.user2 = self.make_user('testuser2')
        self.program_title = 'My program'
        self.day_title = 'First day'
        self.exercise_title = 'First exercise 💪'
        self.program = Program.objects.create(owner=self.user, title=self.program_title)
        self.not_my_program = Program.objects.create(owner=self.user2, title=self.program_title)
        self.day = Day.objects.create(program=self.program, title=self.day_title, ind=1)
        self.not_my_day = Day.objects.create(program=self.not_my_program, title=self.day_title, ind=1)
        self.exercise = Exercise.objects.create(day=self.day, title=self.exercise_title, ind=1)

    def test_owner(self):
        self.assertEqual(
            self.exercise.day.program.owner.username,
            'testuser'  # This is the default username for self.make_user()
        )

    def test__str__(self):
        self.assertEqual(
            self.exercise.__str__(),
            self.exercise_title
        )

    def test_slug(self):
        self.assertEqual(
            self.exercise.slug,
            'First-exercise'
        )

    def test_ind_null(self):
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                Exercise.objects.create(day=self.day, title=self.exercise_title)

    def test_ind_duplicate(self):
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                Exercise.objects.create(day=self.day, title=self.exercise_title + '2', ind=1)

    def test_ind_no_duplicates_between_users(self):
        Exercise.objects.create(day=self.not_my_day, title=self.exercise_title, ind=1)

    def test_title_null(self):
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                Exercise.objects.create(day=self.day, ind=1)

    def test_title_duplicate(self):
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                Exercise.objects.create(day=self.day, title=self.exercise_title, ind=2)

                # def test_get_absolute_url(self):
                #     self.assertEqual(
                #         self.program.get_absolute_url(),
                #         '/programs/my-program/'
                #     )


class TestSet(TestCase):
    def setUp(self):
        self.user = self.make_user()
        self.user2 = self.make_user('testuser2')
        self.program_title = 'My program'
        self.day_title = 'First day'
        self.exercise_title = 'First exercise 💪'
        self.program = Program.objects.create(owner=self.user, title=self.program_title)
        self.not_my_program = Program.objects.create(owner=self.user2, title=self.program_title)
        self.day = Day.objects.create(program=self.program, title=self.day_title, ind=1)
        self.not_my_day = Day.objects.create(program=self.not_my_program, title=self.day_title, ind=1)
        self.exercise = Exercise.objects.create(day=self.day, title=self.exercise_title, ind=1)
        self.not_my_exercise = Exercise.objects.create(day=self.not_my_day, title=self.exercise_title, ind=1)
        self.set = Set.objects.create(exercise=self.exercise, ind=1)

    def test_owner(self):
        self.assertEqual(
            self.set.exercise.day.program.owner.username,
            'testuser'  # This is the default username for self.make_user()
        )

    def test_ind_null(self):
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                Set.objects.create(exercise=self.exercise)

    def test_ind_duplicate(self):
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                Set.objects.create(exercise=self.exercise, ind=1)

    def test_ind_no_duplicates_between_users(self):
        Set.objects.create(exercise=self.not_my_exercise, ind=1)

        # def test_get_absolute_url(self):
        #     self.assertEqual(
        #         self.program.get_absolute_url(),
        #         '/programs/my-program/'
        #     )
