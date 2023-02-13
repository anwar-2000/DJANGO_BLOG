from django.db import models
from django.utils.text import slugify
from django.core.validators import MinLengthValidator


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
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="authorPosts")
    imageName = models.ImageField(upload_to="images")
    date = models.DateField(auto_now=True)
    slug = models.SlugField(db_index=True, null=False)
    content = models.TextField(validators=[MinLengthValidator(10)])
    tag = models.ManyToManyField(Tag, blank=True, related_name='Tags_Post')

    def __str__(self):
        return f"{self.title} ---- {self.date}"

    def save(self, *args, **kwargs):  # this function is to auto populate slug field based on the title
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Comment(models.Model):
    username = models.TextField(max_length=60)
    email = models.EmailField(default=None)
    text = models.TextField(max_length=200)
    post = models.ForeignKey(Post,on_delete=models.CASCADE , related_name="comments",default=None)
    def __str__(self):
        return f"{self.username} => {self.email}"
    