from django.urls import path,include
from .views import ticket_list, ticket_detail
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('tickets/', ticket_list),
    path('tickets/<int:id>/', ticket_detail),
]