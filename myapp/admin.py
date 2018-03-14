from django.contrib import admin

# Register your models here.
from myapp.models import Question

admin.site.register(Question)