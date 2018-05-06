from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class HomeView(View):
    """首页视图类"""
    def get(self,request):
        request.user.is_authenticated()
        return render(request,'home.html')