from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request):
    print(request.user)
    # return HttpResponse("Hello")
    return render(request, 'home.html')

def about_view(request):
    my_context = {
        'title': 'about title',
        'my_text': 'This is About Us',
        'my_number': 123,
        'my_item_list': [111, 222, 333, "Abc"],
        'html_output': '<h4>Html tag</h4>'
    }
    return render(request, 'about.html', my_context)

def contact_view(request):
    return render(request, 'contact.html')

def social_view(request):
    return render(request, 'social.html')