from django.shortcuts import render
# from django.template.loader import get_template
from django.http import HttpResponse

# Create your views here.
def login(request):
    # template = get_template("")
    return HttpResponse(render(request=request, template_name="login.html"))