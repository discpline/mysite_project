from django.contrib import admin
from .models import CourseCategory, Course, Teacher, CompanyHead, Instructor, SendMessage, Comment
from django.utils.html import format_html

admin.site.register(CourseCategory)
admin.site.register(SendMessage)
admin.site.register(Comment)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'category', 'name', 'price', 'students', 'lessons', 'is_visible', 'photo_tag',
                    'photo_next_tag')
    list_editable = ('category', 'name', 'price', 'students', 'lessons',  'is_visible')
    search_fields = ('name',)
    list_filter = ('category', 'price', 'is_visible')

    def photo_tag(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="50" height="auto" />', obj.photo.url)
        return "-"

    photo_tag.short_description = 'Course Photo'

    def photo_next_tag(self, obj):
        if obj.photo_next:
            return format_html('<img src="{}" width="50" height="auto" />', obj.photo_next.url)
        return "-"

    photo_next_tag.short_description = 'Course Next Photo'


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'position', 'description', 'is_visible', 'teacher_photo')
    list_editable = ('name', 'description', 'is_visible')
    search_fields = ('name',)
    list_filter = ('is_visible',)

    def teacher_photo(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="auto" />', obj.image.url)
        return "-"

    teacher_photo.short_description = 'Teacher Photo'


@admin.register(CompanyHead)
class CompanyHeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'is_active', 'head_photo')
    list_filter = ('is_active',)
    search_fields = ('name', 'title')

    def head_photo(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="auto" />', obj.image.url)
        return "-"

    head_photo.short_description = 'Head Photo'


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'is_active', 'photo_instr')
    list_filter = ('is_active',)
    search_fields = ('name',)

    def photo_instr(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="50" height="auto" />', obj.photo.url)
        return "-"

    instructor_photo_description = 'Instructor Photo'




