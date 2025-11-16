from django.shortcuts import render
from django.views import View
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from core.mixins import IsSellerMixin

# Create your views here.

class SellerDashboardView(LoginRequiredMixin, IsSellerMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'seller/dashboard.html')
    
class CustomPasswordChangeView(LoginRequiredMixin, IsSellerMixin, PasswordChangeView):
        template_name = 'seller/password_change.html'
        success_url = reverse_lazy('login')
        
        def form_valid(self, form):
            response =  super().form_valid(form)
            logout(self.request)
            
            messages.success(
                self.request, "Password changed successfully. Please login with your new password.")
            return response
        
        def form_invalid(self, form):
            messages.error(
                self.request, "There was an error changing your password, please try again.")
            return super().form_invalid(form)
