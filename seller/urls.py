from django.urls import path
from seller.views import SellerDashboardView, CustomPasswordChangeView

urlpatterns = [
    path('dashboard/', SellerDashboardView.as_view(), name="seller_dashboard"),
    path('password-change/', CustomPasswordChangeView.as_view(), name="password_change")
]
