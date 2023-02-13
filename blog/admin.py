from django.contrib import admin

# Register your models here.


from .models import Post, Author, Tag


class PostAdmin(admin.ModelAdmin):
    # slug will be generated auto... and not editable through admin Panel
    # readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("date", "author", "tag")
    list_display = ("title", "author", "date",)


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
