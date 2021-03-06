"""neighborlyApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import handler404
from django.contrib import admin
from django.urls import path
from neighborlyUsers import views
from location.views import location_search
from posts import views as post_views
from django.conf import settings
from django.conf.urls.static import static
from notifications import views as notif_views
from comments import views as com_views
from django.views.static import serve
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage_view, name='index'),
    path('register/', views.Register.as_view(), name='signup'),
    path('login/', views.Login_View.as_view(), name='login'),
    path('logout/', views.logout_action, name='logout'),
    path("location/", location_search, name="location"),
    path('addpost/', post_views.add_post_view, name="addpost"),
    path("post/<int:id>/", post_views.Post_Detail_View.as_view(), name="post"),
    path('post/<int:id>/edit/', post_views.edit_post_view, name="editpost"),
    path('notifications/<int:id>/',
         notif_views.notification_view, name="notifications"),
    path('comment/<int:id>/', com_views.create_comment_view, name='comments'),
    path('post/<int:id>/delete/', post_views.delete_post_view, name='delete'),
    path('notifications/<int:id>/',
         notif_views.notification_view, name="notifications"),
    path('profile/<int:id>/', views.user_profile_view, name="profile"),
    path('profile/<int:id>/update/', views.edit_user_view, name="edituser"),
]

handler404 = 'neighborlyUsers.views.error_404_view'
handler500 = 'neighborlyUsers.views.error_500'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
