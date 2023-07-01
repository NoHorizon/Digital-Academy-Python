from django.db import models
from django.urls import reverse
from django.utils import timezone

"""
QuerySet API
to use QuerySet API you have to access static attribute "objects"
ModelName.objects
Post.objects.all() -> all post that is in the database
ModelName.objects.first() -> earliest write in database for this model table
ModelName.objects.last() -> most recent write in database for this model table
ModelName.objects.filter() -> filter  model's table for specific information
* from django.utils import timezone
* Post.objects.filter(id=1)
* Post.objects.filter(create_time__date=timezone.now().date())
* Post.objects.filter(title__icontains="T")
ModelName.objects.get() -> Single object; there should be only one with field you are searching

object / instance methods
* save() -> sync application to database
* refresh_from_db() -> sync changes to application from DB (database)
* delete() -> deletes object from database
"""


# Create your models here.
# ORM - Object Relational Mapping / Mapper
class Post(models.Model):
    author = models.CharField(max_length=120)
    title = models.CharField(max_length=255)
    text = models.TextField()

    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        # magic / dunder methods
        return f'{self.author} - {self.title}'

    def is_recent(self) -> bool:
        return self.create_time.date() == timezone.now().date()

    def get_absolute_url(self) -> str:
        return reverse('blog:post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # one to many
    # ForeignKey creates modelname_set field to the related model
    author = models.CharField(max_length=120)
    text = models.TextField()

    def __str__(self) -> str:
        return f'{self.author} {self.post}'
