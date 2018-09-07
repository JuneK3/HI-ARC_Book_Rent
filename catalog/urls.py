from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.ListAllBooks.as_view(),
        name='all_books',
    ),
    url(
        regex=r'authors/$',
        view=views.ListAllAuthors.as_view(),
        name='all_authors',
    ),
    url(
        regex=r'genres/$',
        view=views.ListAllGenres.as_view(),
        name='all_genres',
    ),
    url(
        regex=r'languages/$',
        view=views.ListAllLanguages.as_view(),
        name='all_languages',
    ),
    url(
        regex=r'intances/$',
        view=views.ListAllBookInstances.as_view(),
        name='all_instances',
    )

]
