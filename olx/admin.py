from django.contrib import admin

# Register your models here.
from olx.models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}
    class Meta:
        model = Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','is_sold','category','seller','image']
    class Meta:
        model = Product

class CartAdmin(admin.ModelAdmin):
    list_display = ['user','product']
    class Meta:
        model = Cart

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','picture','contact_no','address']
    class Meta:
        model = UserProfile

class CommentsAdmin(admin.ModelAdmin):
    list_display = ['user','comments','product']
    class Meta:
        model = Comments

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Cart,CartAdmin)
admin.site.register(UserProfile,ProfileAdmin)
admin.site.register(Comments,CommentsAdmin)