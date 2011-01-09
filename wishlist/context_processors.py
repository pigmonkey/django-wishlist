from wishlist import settings

def processors(request):
    """
    Add wishlist settings to the conext, making them available to templates.
    """
    return {
        'wishlist_title': settings.WISHLIST_TITLE,
        'currency': settings.WISHLIST_CURRENCY[0],
        'currency_symbol': settings.WISHLIST_CURRENCY[1]
    }
