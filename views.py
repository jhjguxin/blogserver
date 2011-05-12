# Create your views here.
from django.shortcuts import render_to_response
import pdb

def base_page(request):
#  pdb.set_trace()
  return render_to_response("base.html",)
