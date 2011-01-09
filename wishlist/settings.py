"""
Settings for the wishlist. These should not be edited directly. Instead,
overwrite them in the main project's setting file.
"""
from django.conf import settings

# The name of the wishlist
WISHLIST_TITLE = getattr(settings, 'WISHLIST_TITLE', 'My Wishlist')

# Currency to list prices in.
# This should be a tuple, with the first item being the currency abbreviation and the
# second item being the currency symbol.
WISHLIST_CURRENCY = getattr(settings, 'WISHLIST_CURRENCY', ('USD', '$'))

# Should all items on the wishlist be public.
WISHLIST_PUBLIC = getattr(settings, 'WISHLIST_PUBLIC', False)

# A tuple of tags which mark the tagged item as being public.
# This is only considered if WISHLIST_PUBLIC above is set to False
WISHLIST_PUBLIC_TAGS = getattr(settings, 'WISHLIST_PUBLIC_TAGS', ('public', 'birthday', 'xmas'))
