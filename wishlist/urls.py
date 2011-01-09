from django.conf.urls.defaults import *
from tagging.views import tagged_object_list
from wishlist.models import Item
from wishlist.views import add_item, delete_item, wishlist, bookmarklet

tags = {
    'queryset_or_model': Item,
    'template_object_name': 'item',
}

urlpatterns = patterns('',
    (r'^add/$', add_item),
    (r'^(?P<id>\d+)/delete/$', delete_item),
    (r'^tag/(?P<tag>[^/]+)/$', tagged_object_list, tags, "items_by_tag"),
    (r'^bookmarklet/$', bookmarklet),
    (r'^sort/(?P<sort_by>\w+)/(?P<sort>\w+)/$', wishlist),
    (r'^$', wishlist),
)
