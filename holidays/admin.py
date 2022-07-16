from django.contrib import admin

from .models import Holiday
from .models import Continent

admin.site.register(Holiday)
admin.site.register(Continent)

