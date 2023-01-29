from email.policy import default
from django.db import models

from django.db.models.signals import pre_save,post_save,pre_delete,post_delete
from django.dispatch import receiver
from sqlalchemy import null
from django.template.defaultfilters import slugify
from datetime import datetime
import json

class Task(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    slug = models.SlugField(max_length=200, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

# def task_handler(sender, instance, **kwargs):
#     print('you printed me')
#     print(instance.name)
#     print(instance.description)
# pre_save.connect(task_handler, sender=Task)

class TaskDate(models.Model):
    task = models.ForeignKey(Task, on_delete = models.CASCADE)
    date = models.CharField(max_length = 100)

class History(models.Model):
    history = models.TextField(default = '{}')

@receiver(pre_save, sender=Task)
def task_handler(sender, instance, **kwargs):
    print('2nd way of writing a signal')
    # print(slugify(instance.name))
    instance.slug = slugify(instance.name)
    # instance.save()

@receiver(post_save, sender = Task)
def task_handler(sender, instance, **kwargs):
    TaskDate.objects.create(task=instance, date = datetime.now())

@receiver(pre_delete, sender = Task)
def task_handler_pre_delete(sender, instance, **kwargs):
    data = {'task': instance.name, 'desc': instance.description, 'slug': instance.slug}
    History.objects.create(history = json.dumps(data))