from .models import MainMenuItems, Footer


def main_menu_items(request):
    """
    Отримання елементів головного меню для контексту шаблону.

    Args:
        request (HttpRequest): Об'єкт запиту.

    Returns:
        dict: Словник з елементами головного меню для передачі в контекст шаблону.
    """
    items = MainMenuItems.objects.filter(is_visible=True)
    return {'main_menu_items': items}


def footer_context(request):
    """
    Отримання контексту для футеру сторінки.

    Args:
        request (HttpRequest): Об'єкт запиту.

    Returns:
        dict: Словник з даними футера для передачі в контекст шаблону.
    """
    footer = Footer.objects.first()
    return {'footer': footer}
