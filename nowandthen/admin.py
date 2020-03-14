from django.contrib import admin
from nowandthen.models import Category, Page, Picture
from nowandthen.models import UserProfile

class PageAdmin(admin.ModelAdmin):
    list_display = ('title','category', 'url')

class PictureAdmin(admin.ModelAdmin):
    list_display = ('image', 'title', 'description', 'tag_one', 'tag_two','era',)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Picture, PictureAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
