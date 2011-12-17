Wishlist
========

Wishlist is a [Django](http://www.djangoproject.com/) application for creating wishlists!


Genesis
-------

Wishlist came about due to dissatisfaction with other wishlist offerings.

I used Amazon Wishlist for a number of years, but my paranoia finally caught up to me and I decided that I didn't need to give Amazon that much more information about my interests.

I tried a few substitutes and found that my requirements for a wishlist were less than common. I don't often use wishlists in the common way of asking people for gifts on special occasions. Instead, I use wishlists privately to keep track of items that I wish to purchase myself. It helps me to determine savings goals, to track books that I want to read, etc. As such, I usually do not want items on my wishlist to be publicly viewable.

Out of the substitutes I tried, [Wishlistr](http://www.wishlistr.com/) was undoubtedly the best, but there were some aspects of it that I didn't like. After using it for a while, I decided to write my own app. Wishlistr inspired parts of this application.


Features
--------


### Tagging

Items may be tagged for organization.


### Priority

Items may be given a priority from 1 (highest) to 5 (lowest).

### Sorting

The list may be sorted by the items' priority, price, or the date they were added.


### Publicity

The whole wishlist can be made to be publicly viewable, or not.

Fine-grained control can be archived with the `WISHLIST_PUBLIC_TAGS` setting, which allows the user to specify public tags. If an item is tagged with a public tag, it will be viewable. For example, all items on the wishlist may be private, except those items tagged with "public" or "birthday".


### Bookmarklet

Wishlist includes a bookmarklet to ease the process of adding items to the list.

While on the page of a product that you would like to add, click the bookmarklet to be taken to Wishlist's add item form. The form will pre-populate itself with the URL of the item page. It will also attempt to scrape the item name and price from the page. This makes adding a new item to the wishlist exceedingly simple: browse to the item page, click the bookmarklet, confirm that the pre-populated information is correct, and submit! After the form is submitted, you will be directed back to the item page so that you may continue your browsing.


Installation
------------

1.  Put the `wishlist` directory somewhere in your Python path (like inside your Django project folder).

2.  Add `wishlist` to your `settings.INSTALLED_APPS`.

3.  Add `wishlist.context_processors.processors` to your `settings.TEMPLATE_CONTEXT_PROCESSORS`.


Requirements
------------

* [django-taggit](http://django-taggit.readthedocs.org) is used for tagging.
* [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/) is used for page parsing.


Configuration
-------------

Wishlist includes a number of settings that you may modify in your project's main `settings` file.


### `WISHLIST_TITLE`

A string containing the name of the wishlist.

Default: 'My Wishlist'


### `WISHLIST_CURRENCY`

A tuple containing the currency abbreviation and symbol that should be used for item prices.

Default: ('USD', '$')


### `WISHLIST_PUBLIC`

A boolean which determines whether all items on the wishlist should be publicly viewable or not.

Default: False


### `WISHLIST_PUBLIC_TAGS`

A tuple of tags which mark the tagged item as being public.

This setting is only considered if `WISHLIST_PUBLIC` is set to False.

Default: ('public',)


Feedback
--------

If you use Wishlist, I'd be interested to hear any feedback you might have. [Contact me via email](mailto:pm@pig-monkey.com).

From the user perspective, I'm keen to hear whether the app fills your needs or not.

I am new to both Django and Python, so, from the developer perspective, I would appreciate any feedback on the code.
