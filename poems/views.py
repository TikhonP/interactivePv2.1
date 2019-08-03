import random

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from poems.models import Poem, Paragraph

def read(request):
    # получаем все закончиенные тексты
    poems = Poem.objects.filter(ended=True)
    if poems.count() == 0:
        return HttpResponse("Пока еще нет готовых.")

    # выбираем случайную
    poem = random.choice(poems)
    paragraphs = Paragraph.objects.filter(poem=poem)

    if "poem" in request.GET:
        id = request.GET['poem']
        poemS = Poem.objects.get(pk=id)
        paragraphs = Paragraph.objects.filter(poem=poemS)
        return render(request, 'indexReadStory.html', {'poem': poemS, 'paragraphs': paragraphs})

    return render(request, 'indexRead.html', {'poem': poem, 'paragraphs': paragraphs, 'poems': poems})




def write(request):
    if request.method == 'GET':
        poems = Poem.objects.filter(ended=False)
        if poems.count() == 0 or "new" in request.GET:
            # создаем новый текст
            poem = Poem()
            poem.save()

            paragraph = Paragraph()
            paragraph.poem = poem
            paragraph.text = ""
            paragraph.save()
        else:
            # выбираем один из текущих
            poem = random.choice(poems)
            paragraphs = Paragraph.objects.filter(poem=poem)
            paragraph = paragraphs.reverse()[0]

        print(poem.title)
        return render(request, 'index.html', {'poem': poem, 'paragraph': paragraph})

    if request.method == 'POST':
        id = request.POST['id']
        # находим нашу поэму с конкретным id...
        poem = Poem.objects.get(pk=id)
        paragraphs = Paragraph.objects.filter(poem=poem)
        paragraph = paragraphs.reverse()[0]

        if paragraph.text != "":
            paragraph = Paragraph()
            paragraph.poem = poem

        if request.POST['button'] == 'добавить':
            paragraph.text = request.POST['text']
            paragraph.author = request.POST['username']
            if poem.title == "Без названия.":
                poem.title = request.POST['title']
        else:
            poem.title = request.POST['title']
            paragraph.text = request.POST['text']
            poem.ended = True
            paragraph.author = request.POST['username']

        # сохраняем
        poem.save()
        paragraph.save()
        return render(request, 'index.html', {'poem': poem, 'paragraph': paragraph})

