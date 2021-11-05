import unittest
from app.models import Source,Article

class SourceTest(unittest.TestCase):
    """Test Class to test the behaviour of the Source class"""

    def setUp(self):
        '''
        Set up method that will run before every test
        '''

        self.new_source = Source("ABC","Get news up by us","English")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))

    def test_correct_instance(self):
        self.assertEqual(self.new_source.name,"ABC")
