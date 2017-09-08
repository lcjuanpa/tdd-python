from selenium import webdriver
import unittest

from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()
    self.browser.implicitly_wait(3)

  def tearDown(self):
    self.browser.close()

  def testCanStartAListAndRetrieveItLater(self):
    # Edith has heard about a cool new online to-do app. She goes to check
    # out its homepage.
    self.browser.get('http://localhost:8000')

    # She notices the page title and header mention to-do lists.
    self.assertIn('To-Do', self.browser.title)
    headerText = self.browser.find_element_by_tag_name('h1').text
    self.assertIn('To-Do', headerText)

    # She is invited to enter a to-do item straight away.
    inputBox = self.browser.find_element_by_id('idNewItem')
    self.assertEqual(inputBox.get_attribute('placeholder'),
        'Enter a to-do item')

    # She types "Buy peacock feathers" into a text box (Edith's hobby is tying
    # flying-fishing lures).
    inputBox.send_keys('Buy peacock feathers')

    # When she hits ENTER, the page updates, and now the page lists:
    # "1: Buy peacock feathers" as an item in a to-do list table.
    inputBox.send_keys(Keys.ENTER)

    table = self.browser.find_element_by_id('idListTable')
    rows = table.find_elements_by_tag_name('tr')
    self.assertTrue(
      any(row.text == '1. Buy peacock feathers' for row in rows))

    # There is still a text box inviting her to add another item. She ENTERS:
    # "Use peacock feathers to make a fly" (Edith is very methodical).
    self.fail('Finish the test!')


if __name__ == '__main__':
  unittest.main(warnings='ignore')




# The page updates again, and now shows both items on her list

# Edith wonders whether the site will remember her list. Then she sees that the
# site has generated a unique URL for her -- there is some explanatory text to
# that effect.

# She visits that URL -her to-do list is still there.

# Satisfied, she goes back to sleep.
