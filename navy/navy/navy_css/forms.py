from django.forms import *

class FrequencyForm(Form):
    sentence = CharField(label='Enter a sentence:')