from django.shortcuts import render
import random


def password_generator(request):
    return render(request, 'Generator/generator.html', {

    })


def get_password(request):
    lowercase_letters = list('abcdefghijklmnopqrstuvwxyz')
    uppercase_letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    special = list('!#$%&*+-=?@^_')
    digits = list('0123456789')
    if request.GET.get('uppercase_letters'):
        lowercase_letters.extend(uppercase_letters)
    if request.GET.get('special'):
        lowercase_letters.extend(special)
    if request.GET.get('digits'):
        lowercase_letters.extend(digits)


    length = int(request.GET.get('length'))
    thepassword = ''
    for i in range(length):
        thepassword += random.choice(lowercase_letters)

    return render(request, 'Generator/password.html', {'password': thepassword,
                                                       })

def info(request):
    return render(request, 'Generator/info.html')