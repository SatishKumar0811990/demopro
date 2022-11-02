
from django.contrib import admin
from django.urls import path, include
from authentication import views
from rest_framework.routers import DefaultRouter

prefix  = "api/v1/"
router = DefaultRouter()
router.register('adminuser',views.Alluser,basename='adminuser')
router.register('linksforadmin',views.linksforadmin,basename="linksforadmin")


urlpatterns = [
    path(prefix + 'admin/', admin.site.urls),
    path(prefix,include(router.urls)),
    path(prefix+'auth/', include('authentication.urls'),name="auth"),
    

]
