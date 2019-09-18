from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^books/(?P<number>[0-9]+)', views.show),
    url(r'^books/new$', views.new_book),
    url(r'^books/addauthor$', views.add_author_to_book),
    url(r'^authors$', views.index_author),
    url(r'^authors/(?P<number>[0-9]+)', views.show_author),
    url(r'^authors/new$', views.new_author),
    url(r'^authors/addbook$', views.add_book_to_author),
]
