from django.contrib import admin
from posts.models import Product, Review

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'create_date', 'modified_date', 'quantity')
    sortable_by = ('price',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Review)