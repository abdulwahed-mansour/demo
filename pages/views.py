from django.views.generic import TemplateView
import json 
from .models import Product
from datetime import datetime
from django.views import generic

import pytz
import random


class HomePageView(TemplateView):
    template_name = 'pages/home.html'
    
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        
        x = '{ "name":"John", "age":30, "city":"New York"}'
        y = json.loads(x)
        
        context['Name'] = y["name"].upper()
        context['Age'] = y["age"]
        context['City'] = y["city"]

      
        # the result is a Python dictionary: print(y["age"])
        return context
    
    
    

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['Product_list'] = Product.objects.all()
        context['local'] = datetime.now().strftime("%d %B %H:%M")
        
        return context
    