from django.urls import path

from .views import home, redirect_url_view, clicked_view

appname = 'shortener'

urlpatterns = [
    path('', home, name='home'),
    path('<str:shortened_part>', redirect_url_view, name='redirect'),
    path('clicked/<str:shortened_part>', clicked_view, name='clicked'),
]
