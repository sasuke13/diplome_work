from django.shortcuts import render
from django.template import TemplateDoesNotExist


def dynamic_template_view(request, template_name):
    # Ensure the template exists or handle any invalid templates
    try:
        return render(request, f'{template_name}.html')
    except TemplateDoesNotExist:
        return render(request, '404.html')
