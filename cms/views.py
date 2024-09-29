from django.shortcuts import render

from .models import UnderDevelopment


def under_development(request):
    main_texts = UnderDevelopment.objects.first()

    return render(request, 'index_cms.html', {'main_texts': main_texts})
