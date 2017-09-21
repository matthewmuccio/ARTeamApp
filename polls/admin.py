from django.contrib import admin

# Tells the admin page that Question objects have an admin interface.

from .models import Question

admin.site.register(Question)