from django.shortcuts import render,HttpResponse
from googletrans import Translator
# from .forms import NameForm
# Create your views here.
lang_dict={
    'afrikaans' : 'af',
'albanian' : 'sq',
'amharic' : 'am',
'arabic' : 'ar',
'armenian' : 'hy',
'azerbaijani' : 'az',
'basque' : 'eu',
'belarusian' : 'be',
'bengali' : 'bn',
'bosnian' : 'bs',
'bulgarian' : 'bg',
'catalan' : 'ca',
'cebuano' : 'ceb',
'chichewa' : 'ny',
'chinese (simplified)' : 'zh-cn',
'chinese (traditional)' : 'zh-tw',
'corsican' : 'co',
'croatian' : 'hr',
'czech' : 'cs',
'danish' : 'da',
'dutch' : 'nl',
'english' : 'en',
'esperanto' : 'eo',
'estonian' : 'et',
'filipino' : 'tl',
'finnish' : 'fi',
'french' : 'fr',
'frisian' : 'fy',
'galician' : 'gl',
'georgian' : 'ka',
'german' : 'de',
'greek' : 'el',
'gujarati' : 'gu',
'haitian creole' : 'ht',
'hausa' : 'ha',
'hawaiian' : 'haw',
'hebrew' : 'he',
'hindi' : 'hi',
'hmong' : 'hmn',
'hungarian' : 'hu',
'icelandic' : 'is',
'igbo' : 'ig',
'indonesian' : 'id',
'irish' : 'ga',
'italian' : 'it',
'japanese' : 'ja',
'javanese' : 'jw',
'kannada' : 'kn',
'kazakh' : 'kk',
'khmer' : 'km',
'korean' : 'ko',
'kurdish (kurmanji)' : 'ku',
'kyrgyz' : 'ky',
'lao' : 'lo',
'latin' : 'la',
'latvian' : 'lv',
'lithuanian' : 'lt',
'luxembourgish' : 'lb',
'macedonian' : 'mk',
'malagasy' : 'mg',
'malay' : 'ms',
'malayalam' : 'ml',
'maltese' : 'mt',
'maori' : 'mi',
'marathi' : 'mr',
'mongolian' : 'mn',
'myanmar (burmese)' : 'my',
'nepali' : 'ne',
'norwegian' : 'no',
'odia' : 'or',
'pashto' : 'ps',
'persian' : 'fa',
'polish' : 'pl',
'portuguese' : 'pt',
'punjabi' : 'pa',
'romanian' : 'ro',
'russian' : 'ru',
'samoan' : 'sm',
'scots gaelic' : 'gd',
'serbian' : 'sr',
'sesotho' : 'st',
'shona' : 'sn',
'sindhi' : 'sd',
'sinhala' : 'si',
'slovak' : 'sk',
'slovenian' : 'sl',
'somali' : 'so',
'spanish' : 'es',
'sundanese' : 'su',
'swahili' : 'sw',
'swedish' : 'sv',
'tajik' : 'tg',
'tamil' : 'ta',
'telugu' : 'te',
'thai' : 'th',
'turkish' : 'tr',
'ukrainian' : 'uk',
'urdu' : 'ur',
'uyghur' : 'ug',
'uzbek' : 'uz',
'vietnamese' : 'vi',
'welsh' : 'cy',
'xhosa' : 'xh',
'yiddish' : 'yi',
'yoruba' : 'yo',
'zulu' : 'zu',
}
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
    inp_lang=request.GET.get('sel_lang', 'en')
    # print(inp_lang)
    lang_code=lang_dict[inp_lang]
    translator = Translator()
    translation = translator.translate(inp_value, dest=lang_code)
    context = {'text': translation.text}
    return render(request,"result.html",context)
    # return HttpResponse(translation.text)
    

    
