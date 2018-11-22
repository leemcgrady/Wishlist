from django.conf.urls import url
from wish.views import WishView

urlpatterns = [

    url(r'^wish$', WishView.as_view(), name='wish'),  # 愿望列表
]

app_name = "wish"

