from django.contrib import admin
from .models import Review, Category, Comment


admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Comment)
