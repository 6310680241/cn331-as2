from django.test import TestCase
from django.urls import reverse, resolve
from assignment.views import course_index, login_index, logout_index

class TestUrls(TestCase):

    def test_coures_url_is_resolve(self):
        url = reverse('view-course')
        print(resolve(url))
        self.assertEquals(resolve(url).func, course_index)

    def test_login_url_is_resolve(self):
        url = reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func, login_index)
    
    def test_logout(self):
        url = reverse('logout')
        print(resolve(url))
        self.assertEquals(resolve(url).func, logout_index)
