from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseForbidden
from django.shortcuts import redirect

class IsBuyerMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and hasattr(self.request.user, 'is_buyer') and self.request.user.is_buyer
    
    def handle_no_permission(self):
        if self.request.user.is_authenticated:
          return HttpResponseForbidden('Access Denied')
        return redirect('login')
    
class IsSellerMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and hasattr(self.request.user, 'is_seller') and self.request.user.is_seller
    
    def handle_no_permission(self):
        if self.request.user.is_authenticated:
          return HttpResponseForbidden('Access Denied')
        return redirect('login')
    