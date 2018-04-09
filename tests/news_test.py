import unnitest
from .models import news
from newsapi import NewsApiClient
News = news.News

class SourceTest(unnitest.TestCase):
    """
    Test Class to test the behaviour of the News class
    """

    def setUp(self):
        """
        set up method that will run before every Test
        """
        self.new_news = newsapi.get_sources()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))

if __name__ == '__main__':
    unnitest.main()