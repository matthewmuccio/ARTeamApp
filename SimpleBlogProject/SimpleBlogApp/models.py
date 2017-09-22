from django.db import models

# Create your models here.
# Tag model that makes and displays tags. 
class Tag(models.Model):
    name = models.CharField(max_length=255) # Name can take any kind of input.
    description = models.CharField(max_length=255, null=True, default='') # Description can take any kind of input.

    def __str__(self):
        return self.name

# Blog model that shows the title, body, and tags of the blog.
class MyBlog(models.Model):
    title = models.CharField(max_length=255) # Title can take any kind of input.
    body = models.CharField(max_length=20000) # Body can take any kind of input.
    tags = models.ManyToManyField(Tag) # Because a blog can be related to multiple tags, and similarly a tag can be used for different blogs.

    def __str__(self):
        return self.title