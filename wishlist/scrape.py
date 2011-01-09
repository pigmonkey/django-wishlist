"""
Functions to scrape item information from a URL.
"""
from wishlist import settings
from BeautifulSoup import BeautifulSoup
from urlparse import urlparse
import re
import urllib2

def get_page(url):
    """
    Opens the given URL and parses it.
    """
    soup = None
    page = None

    # Open the page
    try:
        page = urllib2.urlopen(url)
    except:
        pass
    
    # If the page was opened, parse it
    if page:
        soup = BeautifulSoup(page, convertEntities=BeautifulSoup.HTML_ENTITIES)

    return soup

def name(url, page=None):
    """
    Attempt to scrape the item name from a given url or parsed page.
    """
    name = ''
    # If the URL was not opened, open it.
    if page is None:
        page = get_page(url)

    # If the URL was opened, scrape the page.
    if page:
        # Set the name to the page title.
        name = page.title.contents[0]

        # Amazon specific
        if urlparse(url).netloc == 'www.amazon.com':
            try:
                # Search the DOM for the title.
                # Amazon wraps the title in a span with an id of btAsinTitle.
                name = page.find(id='btAsinTitle').contents[0]
            except:
                pass;
    
    return name.strip()

def price(url, page=None):
    """
    Attempt to scrape the item price from a given url or page.
    """
    currency = settings.WISHLIST_CURRENCY[1]
    price = ''
    
    # If the URL was not opened, open it.
    if page is None:
        page = get_page(url)

    # If the URL was opened, scrape the page.
    if page:
        # If the page contains a string with the currency symbol followed by a
        # digit or dot, set that matching string to the price.
        match = re.search('\%s([.\d]+)' % (currency), str(page))
        if match:
            price = match.group(0)

        # Amazon specific
        if urlparse(url).netloc == 'www.amazon.com':
            try:
                # Search the DOM for the price.
                # Amazon's (horrible) markup looks something like this:
                # <table class="product">
                #   ...
                #   <tr>
                #       <td><b class="priceLarge">$99.99</b>
                #   ...
                price = page.find('table', 'product').findNext('b', 'priceLarge').contents[0]
            except:
                pass;
        
        # If a price was scraped, removed the currency symbol from it.
        if price:
            price = re.sub('\\' + currency, '', price)

    return price.strip()

def item(url):
    """
    Attempts to get the item name and price from a given url
    """
    page = None
    item = {}

    page = get_page(url)

    if page:
        item = {'name': name(url, page), 'price': price(url, page)}

    return item
