from django.contrib import admin
from .models import User
from.models import Movies
from .models import filmbuzz
from .models import Others


class MoviesAdmin(admin.ModelAdmin):
    list_display = ('name', 'release_date', 'imdb_rating', 'movie_director')
    search_fields = ('name', 'movie_director', 'movie_cast', 'movie_genre')
    list_filter = ('release_date', 'movie_language', 'movie_genre')

class filmbuzzAdmin(admin.ModelAdmin):
    list_display = ('fb_title', 'fb_description')

class OthersAdmin(admin.ModelAdmin):
    list_display = ('m_name','m_image','t_link','m_cast')

admin.site.register(filmbuzz, filmbuzzAdmin)
admin.site.register(Movies, MoviesAdmin)
admin.site.register(User)
admin.site.register(Others,OthersAdmin)



