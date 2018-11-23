from django.conf.urls import url
# from user import views
from user.views import RegisterView, LoginView, LogoutView
from user import views

urlpatterns = [
    url(r'^register$', RegisterView.as_view(), name='register'),
    url(r'^login$', LoginView.as_view(), name='login'),
    url(r'^logout$', LogoutView.as_view(), name='logout'),
    url(r'^img_upload/$', views.img_upload, name="img_upload"),
    url(r'^img_handle/$', views.img_handle, name="img_handle"),
]

app_name = "user"

