from django.contrib import admin
from blog.models import BlogsPost,BlogComments

class BlogsPostAdmin(admin.ModelAdmin):
    list_display = ['title','body','timestamp','flag']

class BlogCommentsAdmin(admin.ModelAdmin):
    list_display = ['username','c_content','flag']

admin.site.register(BlogsPost,BlogsPostAdmin)
admin.site.register(BlogComments,BlogCommentsAdmin)

