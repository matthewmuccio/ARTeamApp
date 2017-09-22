from django.db import models
from django.db.models import permalink

# Create your models here.
# A model that creates a database table with the name Blog.
class Blog(models.Model):
    # Fields to be created in the database table.
    title = models.CharField(max_length=100, unique=True) # Title of the blog.
    slug = models.SlugField(max_length=100, unique=True) # Used as the URL to identify the post.
    body = models.TextField() # Contains the body of the blog post.
    posted = models.DateField(db_index=True, auto_now_add=True) # Contains the post date of the post.
    category = models.ForeignKey('blog.Category') # Populates its data from another database table, Category, must populate the Category table first.
    
    # Sets the text reference for each record.
    # Ex: If title is "Matthew's Simple Blog", __unicode__ response is "Matthew's Simple Blog".
    def __unicode__(self):
        return '%s' % self.title

    # Defines a URL for each record in the Blog table.
	# (Without the decorator @permalink it would not work.)
    # Returns a URL calculated from the URLconf file.
    # Ex: If title is "Matthew's Simple Blog", get_absolute_url response is "/SimpleBlogApp/view/matthews-simple-blog".
    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug })

# A model that creates a database table with the name Category.
class Category(models.Model):
    # Fields to be created in the database table.
    title = models.CharField(max_length=100, db_index=True) # Contains the title of the category.
    slug = models.SlugField(max_length=100, db_index=True) # Used as the URL to identify the category.

    # Sets the text reference for each record.
    def __unicode__(self):
        return '%s' % self.title

    # Defines a URL for each record in the Category table.
	# (Without the decorator @permalink it would not work.)
    # Returns a URL calculated from the URLconf file.
    @permalink
    def get_absolute_url(self):
        return ('view_blog_category', None, { 'slug': self.slug })