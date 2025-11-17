from django.db import models

# Create your models here.
# -*- coding: utf-8 -*-
# Models for courses module
from modules.base.models.base import BaseModel 


# Track
class Track(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank = True, null = True)
    def __str__(self):
        return self.name

class Category(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank = True, null = True)
    track=models.ForeignKey(Track, on_delete=models.CASCADE, related_name= "categories", blank=True, null=True)

    def __str__(self):
        return self.name


class SubCategory(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank = True, null = True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name= "subcategories", blank=True, null=True)

    def __str__(self):
        return self.name


# Stage: represents Middle school, High school
class Stage(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2,blank=True, null=True)
    duration = models.DurationField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="stages", blank=True, null=True)
    subcategory=models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name="stages", blank=True, null=True)
    # is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

# Level : grad
class Level(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank = True, null= True)
    order = models.PositiveIntegerField(default=1, blank=True, null=True)
    stage=models.ForeignKey(Stage, on_delete=models.CASCADE, related_name= "levels", blank=True, null=True)

    def __str__(self):
        return self.name

class Subject(BaseModel):
    name = models.CharField(max_length=100,unique=True)
    description = models.TextField(blank = True, null = True)
    Stages=models.ManyToManyField(Stage, related_name="subjects", blank=True)
    categories=models.ManyToManyField(Category, related_name="subjects", blank=True)
    sub_categories=models.ManyToManyField(SubCategory, related_name="subjects", blank=True)

    def __str__(self):
        return self.name

    
class Course(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    track = models.ForeignKey(Track, on_delete=models.CASCADE, related_name= "courses", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name= "courses", blank=True, null=True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name= "courses", blank=True, null=True)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name= "courses", blank=True, null=True)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE, related_name= "courses", blank=True, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name= "courses", blank=True, null=True)
    duration_hours = models.DecimalField(max_digits=5, decimal_places=2, default=0,blank=True, null=True)
    is_published = models.BooleanField(default=False,blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default= 2.00, blank=True, null=True)

    def __str__(self):
        return self.name