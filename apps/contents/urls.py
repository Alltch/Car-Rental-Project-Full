from django.urls import path

from apps.contents.views import (
    home_page, car_detail, contact, feedbacks, terms, autopark
)


urlpatterns = [
    path('', home_page, name='home'),
    path('luma/car/<int:pk>/', car_detail, name='car_detail'),
    path('luma/contact/', contact, name='contact'),
    path('luma/feedbacks/', feedbacks, name='feedbacks'),
    path('luma/terms/', terms, name='terms'),
    path('luma/autopark/', autopark, name='autopark')
]