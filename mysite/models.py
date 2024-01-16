from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.contrib.auth.models import User


class Instructor(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='instructors/')
    description = models.TextField()
    is_active = models.BooleanField(default=True, verbose_name='Is Active')

    def __str__(self):
        return self.name


class CourseCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    order = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Course Categories'
        ordering = ('order',)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    description = models.TextField(blank=True)
    additional_description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='courses/', blank=True, null=True)
    photo_next = models.ImageField(upload_to='courses/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=255, blank=True)
    is_visible = models.BooleanField(default=True)
    order = models.PositiveSmallIntegerField()
    students = models.PositiveIntegerField(default=0)
    lessons = models.PositiveSmallIntegerField(default=0)
    category = models.ForeignKey(CourseCategory, on_delete=models.PROTECT, related_name='courses')
    instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Courses'
        ordering = ('order',)
        constraints = [
            models.UniqueConstraint(fields=['order', 'category'], name='unique_order_per_each_category'),
        ]

    def __str__(self):
        return f'{self.name} - {self.price}$'


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='teachers/')
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class CompanyHead(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    quote = models.TextField()
    image = models.ImageField(upload_to='heads/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Company Head'
        verbose_name_plural = 'Company Heads'


class SendMessage(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    subject = models.TextField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=500, blank=True)

    is_processed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.email}'

    class Meta:
        ordering = ('-created_at', )


class Comment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)




