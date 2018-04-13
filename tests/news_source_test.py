import unittest
from .models import Sources,Articles
from newsapi import NewsApiClient
Sources = sources.Sources

class SourcesTest(unittest.TestCase):
    
        
    def setUp(self):
        """
        set up method that will run before every Test
        """ 
        self.new_sources = Sources("abc-news","ABC News","Your trusted source for breaking news,analysis,exclusive interviews,and videos at ABCNews.com",https://abcnews.go.com,"general","en","us")
         
    def test_instance(self):
        self.assertTrue(isinstance(self.new_sources,Sources))

if __name__ == '__main__':
    unittest.main()