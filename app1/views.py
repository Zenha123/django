from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def disp(request):
 movie_data= {
    'movie': [
    {
        'title':'father',
         'year':1009,
          'summary':"good",
          'success':True
    },
     {
        'title':'father',
         'year':1009,
          'summary':"good",
          'success':True
    },
     {
        'title':'father',
         'year':1009,
          'summary':"good",
          'success':True
    },
     {
        'title':'father',
         'year':1009,
          'summary':"good",
          'success':True
    }
    ]
 }
          
 return render(request,'zen.html',movie_data)
   # return HttpResponse("<b>hello<b>")