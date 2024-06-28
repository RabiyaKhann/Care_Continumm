
from django.urls import path, include
from django.contrib import admin
from .views import authView, home,about,contact,healthcare,blog,predict

urlpatterns = [
 path("", home, name="home"),
 path('admin/', admin.site.urls),
 path("about/", about, name="about"),
 path("contact/", contact, name="contact"),
 path("healthcare/", healthcare, name="healthcare"),
 path("blog/", blog, name="blog"),
 path("signup/", authView, name="authView"),
 path('predict', predict, name='predict'),
 path('contact/', contact, name='contact'),
 path("accounts/", include("django.contrib.auth.urls")),
]
