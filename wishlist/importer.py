from django.contrib.auth.decorators import permission_required
from django.shortcuts import render_to_response
from BeautifulSoup import BeautifulSoup
from wishlist.models import Item
from wishlist.views import scrape_price
import urllib2

@permission_required('wishlist.add_item')
def wishlistr(request, username):
    """
    This is a very rough, hackisk and slow importer for Wishlistr.
    Use at your own risk!
    """
    wishlistr = 'http://www.wishlistr.com/%s' % (username)
    result = None

    # Open the wishlist
    wishlist = urllib2.urlopen(wishlistr)

    # If the wishlist doesn't exist, Wishlistr sends the user to another page.
    # If geturl() returns the original url, we know the wishlist exists.
    if wishlist.geturl() == wishlistr:
        # Parse the wishlist
        soup = BeautifulSoup(wishlist, convertEntities=BeautifulSoup.HTML_ENTITIES)

        # Get all items
        wishlistr_items = soup.ul.findAll('li')

        # Create a list of all wishlistr items
        items = []
        for wishlistr_item in wishlistr_items:
            url = wishlistr_item.contents[2].attrs[1][1]
            price = scrape_price(url)

            # If a price for the item could not be found, set it to 0.
            if price == '':
                price = 0

            items.append({
                'name': wishlistr_item.contents[0].contents[0],
                'url': url,
                'price': price
            })

        # Do some sort of confirmation stuff here
        # ...

        # Add all items to the database
        for item in items:

            # Create the object
            new_item = Item(name=item['name'], price=item['price'], url=item['url'], tags='import, wishlistr')

            # Validate the object
            clean = new_item.full_clean()

            # Save the object
            if clean:
                new_item.save()
                result = 'success?'

    return render_to_response('wishlist/import_wishlistr.html',
        {'items': items, 'result': result},
        context_instance=RequestContext(request))

