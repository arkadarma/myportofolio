from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "I Komang Arka Darma Laksana",
        "npm": "2506656791",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Computer Science student at Universitas Indonesia with an interest in software development, problem solving, and exploring new technologies. I enjoy learning through hands-on projects and continuously improving my technical skills."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "I Komang Arka Darma Laksana",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)