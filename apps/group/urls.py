from django.conf.urls import url
from group.views import GroupView, GroupUserView
urlpatterns = [

    url(r'^group$', GroupView.as_view(), name='group'),  # 分组
    url(r'^user', GroupUserView.as_view(), name='user'),  # 分组用户
]

app_name = "group"

