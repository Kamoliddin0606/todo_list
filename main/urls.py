from django.urls import path
from .views import index, done, remove, reject
urlpatterns = [
    path('', index, name='index'),
    path('done/<int:id>/', done, name='done'),
    path('remove/<int:id>/', remove, name='remove'),
    path('reject/<int:id>/', reject, name='reject'),
]
