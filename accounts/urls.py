from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns =[
    path('signup/',views.SignUp,name="signup"),
    path('signup/worker_signup/',views.WorkerSignUp,name="WorkerSignUp"),
    path('signup/client_signup/',views.ClientSignUp,name="ClientSignUp"),
    path('login/',views.user_login,name="login"),
    path('logout/',views.user_logout,name="logout"),
    path('worker/<int:pk>/',views.WorkerDetailView.as_view(),name="worker_detail"),
    path('client/<int:pk>/',views.ClientDetailView.as_view(),name="client_detail"),
    path('update/worker/<int:pk>/',views.WorkerUpdateView,name="worker_update"),
    path('update/client/<int:pk>/',views.ClientUpdateView,name="client_update"),
    path('change_password/',views.change_password,name="change_password"),
]
