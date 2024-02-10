from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


class MainMenuItems(models.Model):
    """
    Модель елемента головного меню.
    """
    title = models.CharField(max_length=50, verbose_name='menu item')
    slug = models.SlugField(max_length=50, db_index=True, verbose_name='url')
    url = models.CharField(max_length=100, blank=True)
    is_anchor = models.BooleanField(default=False)
    is_manager_only = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=True)
    order = models.PositiveSmallIntegerField()

    def get_absolute_url(self):
        """
        Метод для отримання абсолютного URL для елемента головного меню.

        Returns:
            str: Абсолютний URL елемента головного меню.
        """
        if self.is_anchor:
            return reverse('mysite:home') + f'#{self.slug}'
        return self.slug

    def __str__(self):
        """
        Представлення об'єкта моделі як рядок.

        Returns:
            str: Рядок представлення об'єкта.
        """
        return f'{self.title}/{self.slug}'

    class Meta:
        """
        Клас Meta для налаштувань моделі.
        """
        ordering = ('order', )


class Footer(models.Model):
    """
    Модель футеру сайту.
    """
    address = RichTextField()
    about = RichTextField()
    twitter_link = models.URLField(blank=True)
    facebook_link = models.URLField(blank=True)
    instagram_link = models.URLField(blank=True)
    days = RichTextField(blank=True)
    copyright_text = RichTextField()

    def __str__(self):
        """
        Представлення об'єкта моделі як рядок.

        Returns:
            str: Рядок представлення об'єкта.
        """
        return 'Footer Info'
