from django.contrib import admin
from .models import MainMenuItems, Footer


@admin.register(MainMenuItems)
class MainMenuItemsAdmin(admin.ModelAdmin):
    """
    Налаштування панелі адміністратора для моделі Головного меню.
    """
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'slug', 'is_anchor', 'is_visible', 'order')
    list_editable = ('is_anchor', 'is_visible', 'order')


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    """
    Налаштування панелі адміністратора для моделі Footer.
    """
    list_display = ('address', 'about', 'twitter_link', 'facebook_link', 'instagram_link', 'days', 'copyright_text')
    list_editable = ('about', 'copyright_text', 'days')

