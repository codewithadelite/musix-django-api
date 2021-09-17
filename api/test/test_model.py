from django.test import TestCase
from django.urls import reverse, resolve

from rest_framework.test import APITestCase
from rest_framework import status

from music.models import User, Categories

class TestCategories(TestCase):

	def setUp(self):
		category = Categories.objects.create(name="AFROBEAT")

	def test_insert_category(self):
		
		query = Categories.objects.get(id=1)
		self.assertEqual(query.name, 'AFROBEAT')

class TestUser(APITestCase):
	url = reverse('register')
	def test_user_register(self):
		data = {
			"names":"NIYONSHUTI SHEMA Adelite",
			"username":"shemani",
			"email":"shemani@gmail.com",
			"password":"shemani",
			"password2":"shemani"
		}
		response = self.client.post(self.url,data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(User.objects.count(), 1)
		self.assertEqual(User.objects.get(id=1).username, "shemani")
	def test_user_with_no_confirming_password_cant_register(self):
		data = {
			"names":"NIYONSHUTI SHEMA Adelite",
			"username":"shemani",
			"email":"shemani@gmail.com",
			"password":"shemani",
			"password2":"shemani"
		}
		response = self.client.post(self.url,data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(User.objects.count(), 1)
		self.assertEqual(User.objects.get(id=1).username, "shemani")