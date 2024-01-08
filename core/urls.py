from django.urls import path,include
from django.conf.urls.static import static
from . import views
from dashboard.views import AddTravelViewSet

urlpatterns = [
    path('register/', views.register_view),
    path('login/',views.loginView),
    path('profile-edit/',views.ProfileView),
    path('logout/',views.logoutView),
    path('change-password/',views.passwordEditView),
    path('dashboard/',views.OwnedTravelViewSet),
    path('add-pic/',views.ImageAddView),
    path('dashboard/add-travel/',AddTravelViewSet),
]
