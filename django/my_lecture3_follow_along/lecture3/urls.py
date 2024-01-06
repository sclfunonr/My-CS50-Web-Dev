"""
URL configuration for lecture3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # 'hello/' is the path appears in the browser url.
    # 'hello/' is the module or app 'hello'
    # the "hello" in "hello.urls" is the "hello" module.
    # the "urls" in "hello.urls" is the urls.py file in the hello app.
    path('hello/', include("hello.urls")),
    # How does 'hello/' path maps to "" in urls.py?
    # I think because at this point, there is only one route defined.
    # path('/', include("hello.urls")) # will get 404, "The empty path didn't match any of these"
    path('tasks/', include("tasks.urls") ),
    path('newyear/', include("newyear.urls"))

]
