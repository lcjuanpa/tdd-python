from django.http import HttpRequest
from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import homePage

class HomePageTest(TestCase):

  def testRootUrlResolvesToHomePageView(self):
    found = resolve("/")
    self.assertEqual(found.func, homePage)

  def testHomePageReturnsCorrectHtml(self):
    request = HttpRequest()
    response = homePage(request)
    self.assertTrue(response.content.startswith(b'<html>'))
    self.assertIn(b'<title>To-Do lists</title>', response.content)
    self.assertTrue(response.content.endswith(b'</html>'))
