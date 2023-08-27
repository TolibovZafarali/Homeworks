from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Days of the Week</h1>'
        '<ul>'
            '<li>Monday</li>'
            '<li>Tuesday</li>'
            '<li>Wednesday</li>'
            '<li>Thursday</li>'
            '<li>Friday</li>'
            '<li>Saturday</li>'
            '<li>Sunday</li>'
        '</ul>'    
            )

def english(request):
    return HttpResponse('<h1>Days of the Week(English)</h1>'
        '<ul>'
            '<li>Monday</li>'
            '<li>Tuesday</li>'
            '<li>Wednesday</li>'
            '<li>Thursday</li>'
            '<li>Friday</li>'
            '<li>Saturday</li>'
            '<li>Sunday</li>'
        '</ul>'    
            )

def russian(request):
    return HttpResponse('<h1>Дни Недели(Russian)</h1>'
        '<ul>'
            '<li>Понедельник</li>'
            '<li>Вторник</li>'
            '<li>Среда</li>'
            '<li>Четверг</li>'
            '<li>Пятница</li>'
            '<li>Суббота</li>'
            '<li>Воскресенье</li>'
        '</ul>'    
            )

def uzbek(request):
    return HttpResponse('<h1>Hafta Kunlari(Uzbek)</h1>'
        '<ul>'
            '<li>Dushanba</li>'
            '<li>Seshanba</li>'
            '<li>Chorshanba</li>'
            '<li>Payshanba</li>'
            '<li>Juma</li>'
            '<li>Shanba</li>'
            '<li>Yakshanba</li>'
        '</ul>'    
            )