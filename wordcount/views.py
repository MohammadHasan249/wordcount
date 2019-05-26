from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request, 'homepage.html')


def about(request):
    return render(request, 'about.html')


def count(request):

    text = request.GET['text']
    wordslist = text.split()
    worddict = {}
    for word in wordslist:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1

    sortedwords = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)

    maximum = max(sortedwords, key=operator.itemgetter(1))[0]
    minimum = min(sortedwords, key=operator.itemgetter(1))[0]

    return render(request, 'count.html', {'wordslist': len(wordslist), 'text': text, 'sortedwords': sortedwords,
                                          'maximum': maximum, 'minimum': minimum})

