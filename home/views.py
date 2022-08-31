from django.shortcuts import render, HttpResponse, redirect
from .models import Url
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
import requests

# Create your views here.
def home(request):
    if request.method == "POST":
        url = request.POST.get('MainUrl', False)
        kutted_url = request.POST.get('KuttedUrl', False)
        # print(kutted_url)
        # print(name, url, kutted_url)
        
        if len(str(url)) > 2 and len(str(kutted_url)) > 2:
            correct_url = url
            correct_kutted_url = kutted_url
            form = Url(url=correct_url, redirect_to=correct_kutted_url)
            form.save()
            submitted_form = form

    else:
        submitted_form = ""
        
    all_urls = submitted_form
    print(all_urls)

    params = {'all_urls': all_urls}
    return render(request, 'index.html', params)


def Main_Redirect(request, slug):
    redirection_url = Url.objects.filter(redirect_to=slug)
    if len(redirection_url) == 0:
        return HttpResponse("No Such Url Exists")        
    else:
        val = URLValidator()
        print(val)
        for i in redirection_url:
            try:
                val(i.url)
            except ValidationError as e:
                print('asdafsd')
            print(i.url, i.redirect_to)
        return redirect(str(i.url))

def ViewUrls(request):
    all_urls = Url.objects.all()
    params = {'all_urls': all_urls}
    return render(request, 'urls.html', params)