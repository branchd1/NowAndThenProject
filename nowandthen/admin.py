from django.contrib import admin
from nowandthen.models import Category, Page, Picture, Comment
from nowandthen.models import UserProfile

class PageAdmin(admin.ModelAdmin):
    list_display = ('title','category', 'url')

class PicturesAdmin(admin.ModelAdmin):
    list_display = ('image', 'title', 'description', 'tag_one', 'tag_two','era',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Picture, PicturesAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
