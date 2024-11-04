from django.shortcuts import render
from django.template import TemplateDoesNotExist


def home(request):
    return render(request, 'main.html')


def en_home(request):
    return render(request, 'en/main.html')


def dynamic_template_view(request, template_name):
    try:
        return render(request, f'{template_name}.html')
    except TemplateDoesNotExist:
        return render(request, '404.html')


def english_dynamic_template_view(request, template_name):
    try:
        return render(request, f'en/{template_name}.html')
    except TemplateDoesNotExist:
        return render(request, '404.html')
