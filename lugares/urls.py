"""lugares URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static




from registro.views import (
    CreateLugarAPIView,
    RetrieveLugarAPIView,
    ListLugaresAPIVIEW,
    CreateUsuarioAPIView,
    RetrieveUsuarioAPIView,
    ListLugaresAPIVIEW,
    CreateLikeAPIView,
    CreateDislikeAPIView,

    #LoginView,
    #LogoutView,
)





urlpatterns = [
    path('admin/', admin.site.urls),
    path('lugar/', RetrieveLugarAPIView.as_view()),
    path('lugar/create', CreateLugarAPIView.as_view()),
    path('lugar/edit/<int:formulario_id>/', RetrieveLugarAPIView.as_view()),
    path('lugares/list', ListLugaresAPIVIEW.as_view(),),


    path('usuario/', RetrieveUsuarioAPIView.as_view()),
    path('usuario/create', CreateUsuarioAPIView.as_view()),
    path('usuario/edit/<int:usuario_id>/', RetrieveUsuarioAPIView.as_view()),
    #path('usuarios/list', ListUsuariosAPIVIEW.as_view()),


    path('like/create', CreateLikeAPIView.as_view()),
    #path('like/edit/<int:like_id>/', RetrieveLikeAPIView.as_view(), name='api_add_like'),



    path('dislike/create', CreateDislikeAPIView.as_view()),
    #path('api/add-dislike/<int:like_id>/', RetriveDislikeAPIView.as_view(), name='api_add_dislike'),


    #path('usuruario/signup/', views.SignUpView, name='signup'),
    #path('usuruario/login/', views.LoginView, name='LoginView'),
    #path('usuruario/logout/', views.LogoutView, name='LogoutView'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)