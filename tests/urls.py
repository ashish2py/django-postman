# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from postman.urls import urlpatterns as postman_urls

urlpatterns = [
    url(r'^', include(postman_urls, namespace='postman')),
]
