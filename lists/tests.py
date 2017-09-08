from lists.views import homePage
from django.http import HttpRequest
from django.test import TestCase
from django.core.urlresolvers import resolve
from django.template.loader import render_to_string

class HomePageTest(TestCase):

  def testRootUrlResolvesToHomePageView(self):
    found = resolve("/")
    self.assertEqual(found.func, homePage)

  def testHomePageReturnsCorrectHtml(self):
    request = HttpRequest()
    response = homePage(request)
    # self.assertTrue(response.content.strip().startswith(b'<!DOCTYPE html>')) # strip remove empty lines
    # self.assertIn(b'<title>To-Do lists</title>', response.content)
    # self.assertTrue(response.content.strip().endswith(b'</html>')) # strip remove empty lines
    # b' -> means bytes

    # En lugar de testiar bytes con texto constante, ahora se verifica la
    # logica (con ayuda de una comparacion de cadenas de los contenidos).
    ## One of the rules of unit testing is Don’t test constants, and testing
    ## HTML as text is a lot like testing a constant.
    ## Never do "wibble = 3 | from myprogram import wibble | assert wibble == 3"
    ## Unit tests are really about testing logic, flow control, and configuration.
    expectedHtml = render_to_string('lists/home.html')
    self.assertEqual(response.content.decode(), expectedHtml)
