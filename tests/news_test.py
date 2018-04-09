import unittest
from .models import news
from newsapi import NewsApiClient
News = news.News

class SourceTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the News class
    """

    def setUp(self):
        """
        set up method that will run before every Test
        """
         self.new_news = news("abc-news","ABC News","Your trusted source for breaking news, analysis,exclusive interviews,headlines,and videos at ABCNews.com",http://abcnews.go.com,"general","en","us")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))

if __name__ == '__main__':
    unnitest.main()