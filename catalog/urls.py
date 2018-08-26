from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        regex=r'^all/$',
        view=views.ListAllBooks.as_view(),
        name='all_books',
    ),

]
