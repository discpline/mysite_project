from .models import MainMenuItems, Footer


def main_menu_items(request):
    items = MainMenuItems.objects.filter(is_visible=True)
    return {'main_menu_items': items}


def footer_context(request):
    footer = Footer.objects.first()
    return {'footer': footer}
