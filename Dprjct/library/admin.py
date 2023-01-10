from django.contrib import admin
from .models import Client
from .models import Books
from .models import Location

admin.site.register(Client)
admin.site.register(Books)
admin.site.register(Location)



