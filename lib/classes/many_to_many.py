
class Article:

    all = []

    def __init__(self, author, magazine, title:str):
        if isinstance(title, str) and ( 5 <= len(title) <= 50 ):
            self.author = author
            self.magazine = magazine
            self._title = title
            self.__class__.all.append(self)
        else: 
            raise Exception("Title must be a string of 5-50 characters")

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        raise Exception("Title is immutable")
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, new_author):
        if isinstance (new_author, Author):
            self._author = new_author
        else:
            raise Exception("author must be an Author")
        
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, new_magazine):
        if isinstance (new_magazine, Magazine):
            self._magazine = new_magazine
        else:
            raise Exception("magazine must be a Magazine")
        
class Author:

    all = []

    def __init__(self, name:str):
         if len(name) == 0: 
            raise Exception("Name cannot be empty")
         if hasattr(self, '_name'):
            raise Exception("Name cannot be change changed")
         else:
            self._name = name
            self.__class__.all.append(self)

    @property
    def name(self):
        return self._name

    def articles(self):
        return [ art for art in Article.all if art.author == self]

    def magazines(self):
        return list(set( [art.magazine for art in Article.all if art.author == self] ))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        topic_areas = list(set(mag.category for mag in self.magazines()))
        return topic_areas if topic_areas else None

class Magazine:

    all = []

    def __init__(self, name:str, category:str):
        if not (2 <= len(name) <= 16):
            raise Exception("Name must be 2 - 16 characters long")
        if len(category) == 0:
            raise Exception("Category cannot be empty")
        else:
            self._name = name
            self._category = category
            self.__class__.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name:str):
        if not (2 <= len(new_name) <= 16):
            raise Exception("Name must be 2 - 16 characters long")
        else:
            self._name = new_name
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, new_category:str): 
        if len(new_category) == 0:
            raise Exception("Category cannot be empty")
        else:
            self._category = new_category

    def articles(self):
        return [ art for art in Article.all if art.magazine == self]

    def contributors(self):
        return list(set( [art.author for art in Article.all if art.magazine == self] ))

    def article_titles(self):
        art_titles = list( art.title for art in Article.all if art.magazine == self )
        return art_titles if art_titles else None

    def contributing_authors(self):
        from collections import Counter
        auth_count = Counter(art.author for art in Article.all if art.magazine == self)
        contibs = [ author for author, count in auth_count.items() if count > 2 ]
        return contibs if contibs else None

