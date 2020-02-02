from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time
from django.contrib.postgres.fields import ArrayField

from django.contrib.auth.models import User

def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))

class Task(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('task_detail_url', kwargs={'slug':self.slug})

    def get_update_url(self):
        return reverse('task_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('task_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug

    class Meta:
        ordering = ['-date_pub']

class Test(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE,null=True)
    input = models.CharField(max_length=1000, db_index=True)
    output = models.CharField(max_length=1000, db_index=True)

class Send(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE,null=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=150, db_index=True)
    code = models.TextField(blank=True, db_index=True)
    status = models.CharField(max_length=150, blank=True, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    error = models.TextField(blank=True, db_index=True)


    #def get_absolute_url(self):
        #return reverse('send_detail_url', kwargs={'slug':self.slug})

    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.slug = gen_slug(self.title)
    #     super().save(*args, **kwargs)

    # def __str__(self):
    #     return self.slug
