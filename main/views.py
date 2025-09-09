from django.shortcuts import render

def show_main(request):
    context = {
        'aplikasi' : 'real_mashop',
        'name': 'Raffi Dewangga Susanto',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)