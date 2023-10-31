from django.db import models
from django_quill.fields import QuillField

class Category(models.Model):
    # no usar espacios ya que estas labels van como parte del path
    label = models.CharField(max_length= 100)
    thumbnail = models.ImageField(null=True, blank=True, upload_to="images/categories")
    def __str__(self):
        return self.label

class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length= 255)
    admin_title = models.CharField(max_length= 255, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null = True, blank = True)
    category = models.ManyToManyField(Category)
    thumbnail = models.ImageField(null=True, blank=True, upload_to="images/")
    content = QuillField(null=True, blank=False)
    is_main_content = models.BooleanField(default = False)
    def __str__(self):
        if self.admin_title:
            return self.admin_title 
        else:
            return self.title
