from django.urls import path
from cafe.views import review_list

urlpatterns = [
    path('review_list', review_list, name='review_list'),
]