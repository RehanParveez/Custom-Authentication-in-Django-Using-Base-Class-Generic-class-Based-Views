from django.urls import path
from khata.views import HomeView, LoginView, SubmissionView, activate_account, CustomPasswordResetView, PasswordResetConfirmView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', HomeView.as_view(), name='house'),
    path('login/', LoginView.as_view(), name="login"),
    path('submit/', SubmissionView.as_view(), name="submit"),
    path('activate/<str:uidb64>/<str:token>/', activate_account, name="activate"),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('logout/', LogoutView.as_view(), name="logout")
]
