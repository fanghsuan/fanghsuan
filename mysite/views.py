from django.shortcuts import render
from django.http import HttpResponse
import random

def index(request):
      lucky_no = random.randint(1, 100000)
      
      numbers = list()
      for i in range(1):
          numbers.append(random.randint(1, 100000))
          
      #return HttpResponse("<h3>你今天的幸運號碼是:{}</h3>".format(lucky_no))
      return render(request, "index.html", locals())