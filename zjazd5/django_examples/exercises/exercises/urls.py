"""exercises URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include

from mainpage.views import main_page, hello_world, hello_personalized
from maths.views import calc, math_list, math_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",main_page),
    path("hello",hello_world),
    path("hello/<name>/<lastname>",hello_personalized),
    path("maths",math_list),
    path("maths/<int:id>",math_details),
    path("calc/<operation>/<int:wart1>/<int:wart2>",calc),



]

urlpatterns += [
    path('accounts/', include("django.contrib.auth.urls"))

]