from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    resulttext = (request.POST.get('text', 'default'))
    removepunc = (request.POST.get('removepunc', 'off'))
    fullcap = (request.POST.get('fullcap', 'off'))
    rline = (request.POST.get('rline', 'off'))
    esremover = (request.POST.get('esremover', 'off'))
    charcounter = (request.POST.get('charcounter', 'off'))
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in resulttext:
            if char not in punctuations:
                analyzed = analyzed + char
        args = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        resulttext = analyzed

    if fullcap == "on":
        analyzed = ""
        for char in resulttext:
            analyzed = analyzed + char.upper()
        args = {'purpose': 'Upper Case', 'analyzed_text': analyzed}
        resulttext = analyzed
    if rline == "on":
        analyzed = ""
        for char in resulttext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        args = {'purpose': 'Removed Line', 'analyzed_text': analyzed}
        resulttext = analyzed
    if esremover == "on":
        analyzed = ""
        for end, char in enumerate(resulttext):
            if not (resulttext[end] == " " and resulttext[end + 1] == " "):
                analyzed = analyzed + char
        args = {'purpose': 'Extra Space Remove', 'analyzed_text': analyzed}
        resulttext = analyzed
    if charcounter == "on":
        analyzed = len(resulttext)
        args = {'purpose': 'Character Counter', 'analyzed_text': analyzed}
    if removepunc != "on" and fullcap != "on" and rline != "on" and esremover != "on" and charcounter != "on":
        return HttpResponse("Make Sure That The Checkbox Is Clicked")



    return render(request, 'analyze.html', args)