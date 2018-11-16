from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tinymce/', include('tinymce.urls')), # 富文本编辑器
    url(r'^user/', include(('user.urls', 'user'), namespace='user')),  # 用户模块
    url(r'^group/', include(('group.urls', 'group'), namespace='group')),  # 组模块
    url(r'^wish/', include(('wish.urls', 'wish'), namespace='wish')),  # 愿望模块
]
