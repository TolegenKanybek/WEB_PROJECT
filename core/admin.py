from django.contrib import admin

from core.models import Category, Product

admin.site.register(Product)

@admin.register(Category)

class CategoryAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'created_by',)