from django.urls import path
from django.contrib import admin
from .views import index, done, remove, reject, start
urlpatterns = [
    path('', index, name='index'),
    path('done/<int:id>/', done, name='done'),
    path('remove/<int:id>/', remove, name='remove'),
    path('reject/<int:id>/', reject, name='reject'),
    path('start/<int:id>/', start, name='start'),
    path('update/<int:id>/', index, name='update'),
    path('admin/', admin.site.urls, name='admin'),
]
