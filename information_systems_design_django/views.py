from django.shortcuts import render


def main_page(request):
    return render(request, 'information_systems_design_django/index.html')
