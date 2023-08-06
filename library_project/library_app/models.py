from django.db import models

# Create your models here.
class Author(models.Model):
    author_name=models.CharField(max_length=30,unique=True)
    age=models.IntegerField()
    no_of_awards=models.IntegerField()
    dob=models.DateField()
    author_image=models.ImageField(upload_to='author_images/')
    description=models.TextField()
    def __str__(self):
        return self.author_name
    def get_model_name(self):
        return self.__class__.__name__

class Genre(models.Model):
    genre_name=models.CharField(max_length=20,unique=True)
    def __str__(self):
        return self.genre_name
    def get_model_name(self):
        return self.__class__.__name__


class Book(models.Model):
    book_name=models.CharField(max_length=100,unique=True)
    #one book wiil have one author
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    #one book can have many genre
    genre=models.ManyToManyField(Genre)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    release_date=models.DateField()
    book_image=models.ImageField(upload_to='book_images/')
    description=models.TextField()

    def get_model_name(self):
        return self.__class__.__name__

    def __str__(self):
        return f' Book : {self.book_name} by {self.author}'