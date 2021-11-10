from django.urls import path
from .views import *

urlpatterns = [
    path("register",registration,name="register"),
    path("log", login_page, name="log"),
    path("list",list_employe,name="list"),
    path("edit/<int:id>",EditEmploy,name="edit"),
    path("create",CreateEmploy,name="create"),
    path("filter/<int:id>",FilterEmploy,name="filter")

]