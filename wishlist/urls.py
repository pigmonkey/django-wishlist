from django.conf.urls.defaults import *
from wishlist.models import Item
from wishlist.views import add_item, delete_item, wishlist, bookmarklet

urlpatterns = patterns('',
    (r'^add/$', add_item),
    (r'^(?P<id>\d+)/delete/$', delete_item),
    url(r'^tag/(?P<querytag>[^/]+)/$', view=wishlist, name="items_by_tag"),
    (r'^bookmarklet/$', bookmarklet),
    (r'^sort/(?P<sort_by>\w+)/(?P<sort>\w+)/$', wishlist),
    (r'^$', wishlist),
)
