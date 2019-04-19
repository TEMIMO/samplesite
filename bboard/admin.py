from django.contrib import admin

from .models import Bb
from .models import Rubric
from .models import City

class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rubric', 'city')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content', )

admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric)
admin.site.register(City)
# Register your models here.
