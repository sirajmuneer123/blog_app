from django.contrib import admin
from blog_app.models import Blog,Comment
from blog_app.models import UserProfile
# Register your models here.
class CommentAdmin(admin.ModelAdmin):
	list_display=('blog_title','comment')
class BlogAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('title',)}

admin.site.register(UserProfile)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Comment,CommentAdmin)
