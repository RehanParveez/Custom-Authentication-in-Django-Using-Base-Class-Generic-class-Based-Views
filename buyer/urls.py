from django.urls import path
from buyer.views import BuyerDashboardView, CustomPasswordChangeView

urlpatterns = [
    path('dashboard/', BuyerDashboardView.as_view(), name='buyer_dashboard'),
    path('password-change/', CustomPasswordChangeView.as_view(), name='password_change'),
]
