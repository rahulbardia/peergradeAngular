from django.conf.urls import url, include, patterns
# from rest_framework.urlpatterns import format_suffix_patterns

from peergradeApp.views import PeerNotification
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', PeerNotification.as_view()),
)

# urlpatterns = format_suffix_patterns(urlpatterns)