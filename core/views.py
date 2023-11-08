from django.shortcuts import render, HttpResponse, redirect
from django.views import View

class HomeView(View):
    def get(self, request):
        return render(request, 'core/homepage.html')