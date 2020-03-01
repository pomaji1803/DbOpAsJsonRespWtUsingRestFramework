"""DbOpAsJsonRespWtUsingRestFramework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from WebApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('all/',views.ViewAllProduct.as_view()),
    path('alldj/',views.ViewAllProductDJ.as_view()),

    path('one/<int:Product>',views.ViewOneProduct.as_view()),
    path('onedj/<int:Product>',views.ViewOneProductDJ.as_view()),

    path('insert_one/',views.InsetOneProduct.as_view(),name='insert_one'),

    path('update_one/<Product>',views.UpdateOneProduct.as_view()),
    path('update_one_another/<Product>',views.UpdateOneProductAnotherWar.as_view()),

    path('delete_one/<Product>',views.DeleteOneProduct.as_view()),

]
