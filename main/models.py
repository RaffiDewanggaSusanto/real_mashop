import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('name', 'Name'),
        ('price', 'Price'),
        ('description', 'Description'),
        ('thumbnail', 'Thumbnail'),
        ('category', 'Category'),
        ('is_featured', 'Is_featured'),
        ('rating', 'Rating'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField()
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField()
    is_featured = models.BooleanField()
    rating = models.IntegerField()

    
    def __str__(self):
        return self.title
    
    @property
    def is_news_hot(self):
        return self.news_views > 20
        
    def increment_views(self):
        self.news_views += 1
        self.save()