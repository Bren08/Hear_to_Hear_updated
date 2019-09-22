from django.test import TestCase
from .models import Aid

# Create your tests here.
class ProductTests(TestCase):
    """
    Here we'll define the tests that we'll run against our
    Hearing_aid model
    """

    def test_str(self):
        test_name = Aid(name='A hearing_aid')
        self.assertEqual(str(test_name), 'A hearing_aid')
