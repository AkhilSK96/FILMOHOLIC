from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    phone = models.CharField(max_length=10, primary_key=True) 

    def __str__(self):
        return self.username

class Movies(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='static/')
    release_date = models.DateField()
    imdb_rating = models.CharField(max_length=100)
    movie_director = models.CharField(max_length=200)
    movie_cast = models.CharField(max_length=1000)
    movie_language = models.CharField(max_length=100)
    movie_genre = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class filmbuzz(models.Model):
    fb_image = models.ImageField(upload_to='static/')
    fb_title = models.CharField(max_length=500)
    fb_description = models.TextField(max_length=1000)

    def __str__(self):
        return self.fb_title
    
class Others(models.Model):
    m_image=models.ImageField(upload_to='static/')
    m_name=models.CharField(max_length=500)
    t_link=models.TextField(max_length=1000)
    m_cast=models.CharField(max_length=1000)

    def __str__(self):
        return self.m_name