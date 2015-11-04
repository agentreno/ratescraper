import unittest
import ratescraper
import re

class TestRateScraper(unittest.TestCase):
   def test_invalid_country(self):
      self.assertRaises(ValueError, ratescraper.get_calling_cost, "bananas")

   def test_valid_country(self):
      # Does querying a valid country return something that looks like a cost?
      cost = ratescraper.get_calling_cost("New Zealand")
      self.assertIsNotNone(re.match("£\d\.\d\d", cost))

if __name__ == "__main__":
   unittest.main()
