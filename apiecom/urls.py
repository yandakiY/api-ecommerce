"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.views.generic import TemplateView
from .views import list_category , delete_category , create_category , update_category , get_category

qpp_name = 'apiecom'

urlpatterns = [
    # path('/',)
    path('', TemplateView.as_view(template_name='apiecom/index.html')),
    path('categories' , list_category.as_view() , name='categories_list'), # list of categories
    path('create-category' , create_category.as_view() , name='create_category'), # create new category
    path('<int:pk>/update-category' , update_category.as_view() , name='update-category'), # update a category
    path('<int:pk>/category' , get_category.as_view(), name='get-category'), # get category by id
    path('<int:pk>/delete-category' , delete_category.as_view() , name='delete-category'), # delete category by id
]