from django.contrib import admin
from nowandthen.models import Category, Page, Pictures
from nowandthen.models import UserProfile

class PageAdmin(admin.ModelAdmin):
    list_display = ('title','category', 'url')

class PicturesAdmin(admin.ModelAdmin):
    list_display = ('image', 'title', 'description', 'tag_one', 'tag_two','era',)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Pictures, PicturesAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
