from django.contrib import admin
from .models import CourseCategory, Course, Teacher, CompanyHead, Instructor, SendMessage, Comment
from django.utils.html import format_html

admin.site.register(CourseCategory)
admin.site.register(SendMessage)
admin.site.register(Comment)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """
    Налаштування панелі адміністратора для моделі Course.
    """
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'category', 'name', 'price', 'students', 'lessons', 'is_visible', 'photo_tag',
                    'photo_next_tag')
    list_editable = ('category', 'name', 'price', 'students', 'lessons',  'is_visible')
    search_fields = ('name',)
    list_filter = ('category', 'price', 'is_visible')

    def photo_tag(self, obj: Course) -> str:
        """
        Метод для відображення фотографії курсу в панелі адміністратора.

        Args:
            obj (Course): Об'єкт Course.

        Returns:
            str: HTML-рядок, що містить фотографію курсу.
        """
        if obj.photo:
            return format_html('<img src="{}" width="50" height="auto" />', obj.photo.url)
        return "-"

    photo_tag.short_description = 'Course Photo'

    def photo_next_tag(self, obj: Course) -> str:
        """
        Метод для відображення наступної фотографії курсу в панелі адміністратора.

        Args:
            obj (Course): Об'єкт Course.

        Returns:
            str: HTML-рядок, що містить наступну фотографію курсу.
        """
        if obj.photo_next:
            return format_html('<img src="{}" width="50" height="auto" />', obj.photo_next.url)
        return "-"

    photo_next_tag.short_description = 'Course Next Photo'


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    """
    Налаштування панелі адміністратора для моделі Викладач.
    """
    list_display = ('id', 'name', 'position', 'description', 'is_visible', 'teacher_photo')
    list_editable = ('name', 'description', 'is_visible')
    search_fields = ('name',)
    list_filter = ('is_visible',)

    def teacher_photo(self, obj: Teacher) -> str:
        """
        Метод для відображення фотографії викладача в панелі адміністратора.

        Args:
            obj (Teacher): Об'єкт Викладач.

        Returns:
            str: HTML-рядок, що містить фотографію викладача.
        """
        if obj.image:
            return format_html('<img src="{}" width="50" height="auto" />', obj.image.url)
        return "-"

    teacher_photo.short_description = 'Teacher Photo'


@admin.register(CompanyHead)
class CompanyHeadAdmin(admin.ModelAdmin):
    """
    Налаштування панелі адміністратора для моделі Голова компанії.
    """
    list_display = ('name', 'title', 'is_active', 'head_photo')
    list_filter = ('is_active',)
    search_fields = ('name', 'title')

    def head_photo(self, obj: CompanyHead) -> str:
        """
        Метод для відображення фотографії голови компанії в панелі адміністратора.

        Args:
            obj (CompanyHead): Об'єкт Голова компанії.

        Returns:
            str: HTML-рядок, що містить фотографію голови компанії.
        """
        if obj.image:
            return format_html('<img src="{}" width="50" height="auto" />', obj.image.url)
        return "-"

    head_photo.short_description = 'Head Photo'


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    """
    Налаштування панелі адміністратора для моделі Інструктор.
    """
    list_display = ('name', 'description', 'is_active', 'photo_instr')
    list_filter = ('is_active',)
    search_fields = ('name',)

    def photo_instr(self, obj: Instructor) -> str:
        """
        Метод для відображення фотографії інструктора в панелі адміністратора.

        Args:
            obj (Instructor): Об'єкт Інструктор.

        Returns:
            str: HTML-рядок, що містить фотографію інструктора.
        """
        if obj.photo:
            return format_html('<img src="{}" width="50" height="auto" />', obj.photo.url)
        return "-"

    instructor_photo_description = 'Instructor Photo'




