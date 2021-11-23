from django.shortcuts import render,HttpResponse
from googletrans import Translator
# from .forms import NameForm
# Create your views here.
def index(request):
    # translator = Translator()
    # translation = translator.translate("आप कैसे हैं", dest='en')
    # print(translation.text)
    context={
        'variable':"WELCOME TO THE TRANSLATOR",
    }
    return render(request,"index.html",context)

def translate(request):
    inp_value = request.GET.get('xtext', 'This is a default value')
    translator = Translator()
    translation = translator.translate(inp_value, dest='en')
    context = {'inp_value': inp_value}
    return HttpResponse(translation.text)
    

    
