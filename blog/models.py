from django.db import models
from django.utils.text import slugify
# Create your models here.


class Tag(models.Model):
    caption = models.CharField(max_length=15)

    def __str__(self):
        return f"#{self.caption}"

class Author(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"

class Post(models.Model):
    title = models.CharField(max_length=70)
    excerpt = models.CharField(max_length=120)
    author = models.ForeignKey(Author , on_delete=models.PROTECT ,null=True,related_name="author_posts")
    imageName = models.CharField(max_length=120)
    date = models.DateField(auto_now=True)
    slug=models.SlugField(db_index=True,null=False)
    content = models.CharField(max_length=2500)
    tag = models.ManyToManyField(Tag,blank=True)

    def __str__(self):
        return f"{self.title} ---- {self.date}"

    def save(self,*args, **kwargs): #this function is to auto populate slug field based on the title
        self.slug=slugify(self.title)
        super().save(*args, **kwargs)