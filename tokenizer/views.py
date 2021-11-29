import json
import string
import contractions
from pycountry import languages

from django.http import HttpResponse
from django.http.response import HttpResponseBadRequest

from nltk.tokenize import word_tokenize

from utils.error_object import error_object
from utils.detect_language import detect_language


def tokenizer(request):
    """
    API endpoint that returns a tokenized version of a given text
    """
    try:
        req_data = json.loads(request.body)
    except:
        return HttpResponseBadRequest(error_object('No data'))

    # Validate text information
    if 'text' not in req_data.keys():
        return HttpResponseBadRequest(error_object('No text'))
    else:
        text = str(req_data['text'])

    # Validate language information
    if 'lang' not in req_data.keys():
        lang = detect_language(text)
    elif languages.get(alpha_2=req_data['lang']):
        lang = req_data['lang']
    else:
        return HttpResponseBadRequest(error_object('Bad language. Alpha 2'))

    # Expand the contractions in english
    if lang == 'en':
        text = contractions.fix(text)

    words = word_tokenize(text)
    punctuation = [ char for char in string.punctuation ]
    tokens = [ word for word in words if word not in punctuation ]

    res_data = {'tokens': tokens, 'lang': lang}
    return HttpResponse(json.dumps(res_data))
