from django.core import serializers
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from main.forms import ProjectForm
from main.models import Experience, Project


def show_main(request):
    context = {
        "name": "I Komang Arka Darma Laksana",
        "npm": "2506656791",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Computer Science student at Universitas Indonesia with an interest "
            "in software development, problem solving, and exploring new "
            "technologies. I enjoy learning through hands-on projects and "
            "continuously improving my technical skills."
        ),
    }

    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "I Komang Arka Darma Laksana",
        "experience_list": Experience.objects.all(),
    }

    return render(request, "experience.html", context)


def show_projects(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )

    projects = [project.object for project in projects]

    name_query = request.GET.get("name", "").strip()

    context = {
        "name": "I Komang Arka Darma Laksana",
        "project_list": projects,
        "name_query": name_query,
    }

    return render(request, "projects.html", context)


def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "I Komang Arka Darma Laksana",
        "form": form,
    }

    return render(request, "projects_form.html", context)

def get_projects_json(request):
    name_query = request.GET.get("name", "").strip()
    projects = Project.objects.all()

    if name_query:
        projects = projects.filter(name__icontains=name_query)

    projects_json = serializers.serialize("json", projects)

    return HttpResponse(
        projects_json,
        content_type="application/json",
    )

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")