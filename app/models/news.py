class News:
    """
    news class to define news Objects
    """

    def __init__(self,id,name,description,url,category,language,country):
        self.id = id
        self.name = name
        self.description = description
        self.url = 'https://newsapi.org/v2/sources'
        self.category = category
        self.language = language
        self.country = country
