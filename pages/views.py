from django.views.generic import TemplateView
import json 
from .models import Product
from datetime import datetime
from django.views import generic

from datetime import datetime
import pytz
import random


class HomePageView(TemplateView):
    template_name = 'pages/home.html'
    
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # random.randrange(start, stop, step) 
        context['number'] = random.randrange(0, 100, 5)
        context['local'] = datetime.now().strftime("%m/%d/%Y, %H:%M")
        
        tz_NY = pytz.timezone('America/New_York') 
        datetime_NY = datetime.now(tz_NY)
        context['newyourk'] = datetime_NY.strftime("%m/%d/%Y, %H:%M:%S")
        context['calculation'] = str(8 + 7)
        basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
       
        context['mybaskt'] = basket 
        
        x = '{ "name":"John", "age":30, "city":"New York"}'
        y = json.loads(x)
        
        context['Name'] = y["name"].upper()
        context['Age'] = y["age"] * 5
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
    