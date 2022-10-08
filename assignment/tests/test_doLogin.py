from django.contrib.auth.models import User
from django.test import TestCase

class doLogInTest(TestCase):
    def setUp(self):
        self.testuser = {
            'username': 'admin',
            'password': 'admin'}
        User.objects.create_superuser(**self.testuser)
        
    def test_login(self):
        response = self.client.post('/login', self.testuser, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)
        
    def test_login_is_staff(self):
        response = self.client.post('/login', self.testuser, follow=True)
        self.assertTrue(response.context['user'].is_staff)
