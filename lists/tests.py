from lists.views import homePage
from lists.models import Item

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
    self.assertIn(response.content.decode(), expectedHtml)

  def testHomePageCanSaveAPostRequest(self):
    # Un test no utiliza un browser para hacer solicitudes por tanto, utilizar
    # objetos Request para enviar informacion al servidor.
    request = HttpRequest()
    request.method = 'POST'
    request.POST['itemText'] = 'A new list item'

    response = homePage(request)

    self.assertEqual(Item.objects.count(), 1)
    newItem = Item.objects.first()
    self.assertEqual(newItem.text, 'A new list item')

    # self.assertIn('A new list item', response.content.decode())
    # expectedHtml = render_to_string(
    #   'lists/home.html',
    #   {'newItemText': 'A new list item'}
    # )
    # self.assertEqual(response.content.decode(), expectedHtml)

  def testHomePageRedirectsAfterPost(self):
    request = HttpRequest()
    request.method = 'POST'
    request.POST['itemText'] = 'A new list item'
    response = homePage(request)
    self.assertEqual(response.status_code, 302)
    self.assertEqual(response['location'], '/')

  def testHomePageOnlySavesItemsWhenNecessary(self):
    request = HttpRequest()
    homePage(request)
    self.assertEqual(Item.objects.count(), 0)

  def testHomePageDisplaysAllListItems(self):
    Item.objects.create(text='item 1')
    Item.objects.create(text='item 2')
    request = HttpRequest()
    response = homePage(request)
    self.assertIn('item 1', response.content.decode())
    self.assertIn('item 2', response.content.decode())


class ItemModelTest(TestCase):

  def testSavingAndRetrievingItems(self):
    firstItem = Item()
    firstItem.text = 'The first (ever) list item'
    firstItem.save()

    secondItem = Item()
    secondItem.text = 'Item the second'
    secondItem.save()

    savedItems = Item.objects.all()
    self.assertEqual(savedItems.count(), 2)

    firstSavedItem = savedItems[0]
    secondSavedItem = savedItems[1]
    self.assertEqual(firstSavedItem.text, 'The first (ever) list item')
    self.assertEqual(secondSavedItem.text, 'Item the second')
