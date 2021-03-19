from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login', views.Loginuser.as_view(), name='login'),
    path('register',views.RegisterPage.as_view(),name='register'),
    path('', views.TaskList, name='tasks'),
    path('task/<int:pk>', views.TaskDetail.as_view(), name='task'),
    path('create', views.TaskCreate.as_view(), name='create'),
    path('update/<int:pk>', views.TaskUpdate.as_view(), name='update'),
    path('Delete/<int:pk>', views.TaskDelete.as_view(), name='delete'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
]
