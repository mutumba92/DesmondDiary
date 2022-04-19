from django.contrib import admin
from . models import *

# Register your models here.
admin.site.register(Owner)
admin.site.register(Notes)
admin.site.register(Todos)
admin.site.register(People)