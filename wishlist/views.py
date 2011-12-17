from django.contrib.auth.decorators import permission_required
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.template import RequestContext
from wishlist.models import Item
from wishlist.forms import AddItem, DeleteItem
from wishlist import scrape
from wishlist import settings

def querysort(sort, sort_by):
    """
    Sort Item queries by a field (sort_by) and order (sort)
    """
    if sort == 'asc':
        return Item.objects.all().order_by(sort_by)
    elif sort == 'desc':
        return Item.objects.all().order_by('-' + sort_by)
    else:
        raise Http404

def wishlist(request, sort='desc', sort_by=None, querytag=None):
    """
    Display the wishlist, taking public options and sorting into account.
    """

    # Define available fields to sort by.
    sort_fields = ('priority', 'price', 'date',)

    # Sort the query if a propper request was received.
    if sort_by in sort_fields:
        queryset = querysort(sort, sort_by)
    else:
        queryset = Item.objects.all()

    # If a query tag was provided, create a list of all items tagged with that
    # tag.
    if querytag:
        tagged_items = []
        for item in queryset:
            for tag in item.tags.all():
                if tag.name == querytag:
                    tagged_items.append(item)
                    break
        # Overwrite the queryset with the list of matching items.
        queryset = tagged_items
            

    # If the wishlist is not public and the user does not have permission to
    # change items, set queryset to only include items with public tags.
    if request.user.has_perm('wishlist.change_item') is False and settings.WISHLIST_PUBLIC is False:
        # Get all public tags.
        public_tags = settings.WISHLIST_PUBLIC_TAGS

        # If the item is tagged with a public tag, add it to the public list.
        public_items = []
        for item in queryset:
            for tag in item.tags.all():
                if tag.name in public_tags:
                    public_items.append(item)
                    break

        # Overwrite the original queryset with the list of public items.
        queryset = public_items

    # Return the queryset.
    return render_to_response('wishlist/item_list.html',
        {'item_list' : queryset, 'order': sort, 'sort_by': sort_by, 'sort_fields': sort_fields},
        context_instance=RequestContext(request))

@permission_required('wishlist.delete_item')
def delete_item(request, id):
    """
    Delete an item.
    """

    # Make sure the requested item exists.
    item = get_object_or_404(Item, id=id)
    
    if request.method == 'POST':
        form = DeleteItem(request.POST)
        if form.is_valid():
            item.delete()
            return HttpResponseRedirect(reverse('wishlist.views.wishlist'))
    else:
        form = DeleteItem()
    return render_to_response('wishlist/delete_item.html',
        {'form': form, 'item': item}, context_instance=RequestContext(request))

@permission_required('wishlist.add_item')
def add_item(request, url=None):
    """
    Add an item to the wishlist.
    """
    initial = {}

    # If a URL was passed, use it to get information about the item.
    if 'url' in request.GET:
        url = request.GET['url']
        initial['url'] = url

        # Get the scraped information 
        scraped = scrape.item(url)

        if scraped:
            initial['name'] = scraped['name']
            initial['price'] = scraped['price']

    if request.method == 'POST':
        form = AddItem(request.POST)
        if form.is_valid():
            new_item = form.save()
            if 'url' in request.GET:
                return HttpResponseRedirect(request.GET['url'])
            else:
                return HttpResponseRedirect(reverse('wishlist.views.wishlist'))
    else:
        form = AddItem(initial=initial)
    return render_to_response('wishlist/add_item.html',
        {'form': form, 'url': url},
        context_instance=RequestContext(request))

def bookmarklet(request):
    """
    Display the bookmarklet.
    """

    # Build an absolute URL of the add item form.
    add_url = request.build_absolute_uri(reverse('wishlist.views.add_item'))

    return render_to_response('wishlist/bookmarklet.html', {'add_url': add_url},
        context_instance=RequestContext(request))
