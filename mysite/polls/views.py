from glob import escape
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils.html import escape
from django.views import View
from django.urls import reverse, reverse_lazy
import html
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def index(request):
    return HttpResponse("Hello, world. you are at the polls index")

def funcky(request):
    response = """<html><body><p>This is the funky function sample</p>
    <p>This sample code is available at
    <a href="https://github.com/csev/dj4e-samples">
    https://github.com/csev/dj4e-samples</a></p>
    </body></html>"""
    return HttpResponse(response)

def danger(request, guess):
    response = """<html><body><p>This is the funky function sample</p>
    <p>This sample code is available at"""+escape(guess)+"""
    <a href="https://github.com/csev/dj4e-samples">
    https://github.com/csev/dj4e-samples</a></p>
    </body></html>"""
    return HttpResponse(response)

class MainView(View):
    def get(self, request, guess):
        response = """<html><body><p>Hello world MainView in HTML</p>
        <p>This sample code is available at """+escape(guess)+"""
        <a href="https://github.com/csev/dj4e-samples">
        https://github.com/csev/dj4e-samples</a></p>
        </body></html>"""
        return HttpResponse(response)

def bounce(request) :
    return HttpResponseRedirect('https://www.dj4e.com/simple.htm')

class GameView(View):
    def get(self, request, guess):
        x = {'guess': int(guess)}
        return render(request, 'poll/cond2.html', x)

def guess(request):
    context = {'zap': 45,
                'txt': '<b>bold<b>'}
    return render(request, 'poll/guess.html', context)

def loop(request):
    f = ['Apple', 'Orange', 'Banana', 'Lychee']
    n = ['peanut', 'cashew']
    p = {'outer': {'inner': '42'}}
    x = {'fruits' : f, 'nuts' : n, 'zap' : '42', 'obj': p }
    return render(request, 'poll/loop.html', x)


class SecondView(View):
    def get(self, request):
        u = reverse_lazy('polls:cats')
        u2 = reverse_lazy('polls:dogs')
        u3 = reverse('polls:dog', args=['42'])
        ctx = {'x1': u, 'x2': u2, 'x3': u3}
        return render(request, 'poll/second.html', ctx)


def checkguess(guess):
    msg = False
    if guess:
        try:
            if int(guess) < 42:
                msg = 'Guess too low'
            elif int(guess) > 42:
                msg = 'Guess too high'
            else:
                msg = 'Congratulations!'
        except:
            msg = 'Bad format for guess:' + html.escape(guess)
    return msg

class ClassyView(View):
    def get(self, request):
        return render(request, 'poll/guesspost.html')

    def post(self, request):
        guess = request.POST.get('guess')
        msg = checkguess(guess)
        return render(request, 'poll/guesspost.html', {'message' : msg })






