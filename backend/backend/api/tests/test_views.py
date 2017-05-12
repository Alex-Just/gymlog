from django.db import transaction
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ...core.models import Program
from ...users.models import User


class ProgramTests(APITestCase):
    @classmethod
    def setUpClass(cls):
        super(ProgramTests, cls).setUpClass()
        cls.user = User.objects.get_or_create(username='testuser')[0]
        cls.user.is_active = True
        cls.user.save()

        cls.user2 = User.objects.get_or_create(username='testuser2')[0]
        cls.user2.is_active = True
        cls.user2.save()

        cls.program_title = 'My program 💪'
        cls.program_slug = 'My-program'

    def create_program(self):
        url = reverse('api:program-list')
        data = {'title': self.program_title}

        return {
            'resp': self.client.post(url, data, format='json'),
            'url': url,
        }

    def test_create_program_by_anonym(self):
        resp = self.create_program()['resp']

        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Program.objects.count(), 0)

    def test_create_program(self):
        self.client.force_authenticate(user=self.user)

        resp = self.create_program()['resp']

        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Program.objects.count(), 1)

        program = Program.objects.get()
        self.assertEqual(program.title, self.program_title)
        self.assertEqual(program.slug, self.program_slug)

    def test_view_list_by_anonym(self):
        url = reverse('api:program-list')

        resp = self.client.get(url)

        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(resp.data, {'detail': 'Authentication credentials were not provided.'})

    def test_view_my_list_by_another_user(self):
        self.client.force_authenticate(user=self.user)

        url = self.create_program()['url']

        self.client.logout()
        self.client.force_authenticate(user=self.user2)

        resp = self.client.get(url)

        self.assertEqual(resp.data, [])

    def test_view_my_list(self):
        self.client.force_authenticate(user=self.user)

        url = self.create_program()['url']

        resp = self.client.get(url)
        program = dict(resp.data[0])

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(program['title'], self.program_title)
        self.assertEqual(program['slug'], self.program_slug)

    def test_view_item_by_anonym(self):
        self.client.force_authenticate(user=self.user)
        self.create_program()
        self.client.logout()

        url = reverse('api:program-detail', kwargs={'pk': 1})

        resp = self.client.get(url)

        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(resp.data, {'detail': 'Authentication credentials were not provided.'})

    def test_view_item_by_another_user(self):
        self.client.force_authenticate(user=self.user)
        item = dict(self.create_program()['resp'].data)
        self.client.logout()
        self.client.force_authenticate(user=self.user2)

        url = reverse('api:program-detail', kwargs={'pk': item['id']})

        resp = self.client.get(url)

        self.assertEqual(resp.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(resp.data, {'detail': 'Not found.'})

    def test_view_my_item(self):
        self.client.force_authenticate(user=self.user)
        item = dict(self.create_program()['resp'].data)

        url = reverse('api:program-detail', kwargs={'pk': item['id']})

        resp = self.client.get(url)
        program = dict(resp.data)

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(program['title'], self.program_title)
        self.assertEqual(program['slug'], self.program_slug)

    def test_view_my_item_by_slug(self):
        self.client.force_authenticate(user=self.user)
        item = dict(self.create_program()['resp'].data)

        url = reverse('api:program-detail', kwargs={'pk': item['slug']})

        resp = self.client.get(url)
        program = dict(resp.data)

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(program['title'], self.program_title)
        self.assertEqual(program['slug'], self.program_slug)

    def test_update_item_by_anonym(self):
        self.client.force_authenticate(user=self.user)
        self.create_program()
        self.client.logout()

        url = reverse('api:program-detail', kwargs={'pk': 1})

        resp = self.client.put(url, data={'title': self.program_title + '2'})

        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(resp.data, {'detail': 'Authentication credentials were not provided.'})

    def test_update_item_by_another_user(self):
        self.client.force_authenticate(user=self.user)
        item = dict(self.create_program()['resp'].data)
        self.client.logout()
        self.client.force_authenticate(user=self.user2)

        url = reverse('api:program-detail', kwargs={'pk': item['id']})

        resp = self.client.put(url, data={'title': self.program_title + '2'})

        self.assertEqual(resp.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(resp.data, {'detail': 'Not found.'})

    def test_update_my_item(self):
        self.client.force_authenticate(user=self.user)
        item = dict(self.create_program()['resp'].data)

        url = reverse('api:program-detail', kwargs={'pk': item['id']})

        resp = self.client.put(url, data={'title': self.program_title + '2'})
        program = dict(resp.data)

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(program['title'], self.program_title + '2')
        self.assertEqual(program['slug'], self.program_slug + '-2')

    def test_delete_item_by_anonym(self):
        self.client.force_authenticate(user=self.user)
        self.create_program()
        self.client.logout()

        url = reverse('api:program-detail', kwargs={'pk': 1})

        resp = self.client.delete(url)

        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(resp.data, {'detail': 'Authentication credentials were not provided.'})

    def test_delete_item_by_another_user(self):
        self.client.force_authenticate(user=self.user)
        item = dict(self.create_program()['resp'].data)
        self.client.logout()
        self.client.force_authenticate(user=self.user2)

        url = reverse('api:program-detail', kwargs={'pk': item['id']})

        resp = self.client.delete(url)

        self.assertEqual(resp.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(resp.data, {'detail': 'Not found.'})

    def test_delete_my_item(self):
        self.client.force_authenticate(user=self.user)
        item = dict(self.create_program()['resp'].data)

        url = reverse('api:program-detail', kwargs={'pk': item['id']})

        resp = self.client.delete(url)

        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)

        with self.assertRaises(Program.DoesNotExist):
            with transaction.atomic():
                Program.objects.get(pk=item['id'])


class UserTests(APITestCase):
    @classmethod
    def setUpClass(cls):
        super(UserTests, cls).setUpClass()
        cls.user = User.objects.get_or_create(username='testuser')[0]
        cls.user.is_active = True
        cls.user.save()

        cls.user2 = User.objects.get_or_create(username='testuser2')[0]
        cls.user2.is_active = True
        cls.user2.save()

    def test_view_item_by_anonym(self):
        url = reverse('api:user-detail', kwargs={'pk': 1})

        resp = self.client.get(url)

        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(resp.data, {'detail': 'Authentication credentials were not provided.'})

    def test_view_item_by_another_user(self):
        self.client.force_authenticate(user=self.user2)

        url = reverse('api:user-detail', kwargs={'pk': self.user.id})

        resp = self.client.get(url)
        user = dict(resp.data)

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(user['username'], self.user.username)

    def test_view_my_item(self):
        self.client.force_authenticate(user=self.user)

        url = reverse('api:user-detail', kwargs={'pk': self.user.id})

        resp = self.client.get(url)
        user = dict(resp.data)

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(user['username'], self.user.username)

    def test_view_non_existing_item(self):
        self.client.force_authenticate(user=self.user)

        url = reverse('api:user-detail', kwargs={'pk': -self.user.id})

        resp = self.client.get(url)
        user = dict(resp.data)

        self.assertEqual(resp.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(user, {'detail': 'Not found.'})

    def test_view_my_item_by_current_query(self):
        self.client.force_authenticate(user=self.user)

        url = reverse('api:user-detail', kwargs={'pk': 'current'})

        resp = self.client.get(url)
        user = dict(resp.data)

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(user['username'], self.user.username)

    def test_view_my_item_by_username(self):
        self.client.force_authenticate(user=self.user)

        url = reverse('api:user-detail', kwargs={'pk': self.user.username})

        resp = self.client.get(url)
        user = dict(resp.data)

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(user['username'], self.user.username)
