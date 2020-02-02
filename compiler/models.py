from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time

class Solution(models.Model):
    code = models.TextField(max_length=1000, blank=True, db_index=True)
    input = models.TextField(max_length=3000, blank=True, db_index=True)
    resrun = models.CharField(max_length=2000, blank=True, db_index=True)
    rescomp = models.CharField(max_length=2000, blank = True, db_index=True)
    #input = models.TextField(db_index=True)
    #slug = models.SlugField(blank=True, unique=True)
    #date_pub = models.DateTimeField(auto_now_add=True)

    #def get_absolute_url(self):
    #    return reverse('compiler_view_url', kwargs={'slug':self.slug})

    #class Meta:
    #    ordering = ['-date_pub']
