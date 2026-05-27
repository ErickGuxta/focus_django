from django.urls import path
from . import views

urlpatterns = [
    path('',                 views.index , name = "list-users"  ),
    path('create/'         , views.create, name = "create-users"),
    path('<int:id>/detail/', views.detail, name = "detail-users"),
    path('<int:id>/edit/'  , views.edit  , name = "edit-users"  ),
    path('<int:id>/delete/', views.delete, name = "delete-users")
]
