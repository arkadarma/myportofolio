from django.utils import timezone
from django.core import serializers
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render

from main.forms import ProjectForm, ExperienceForm
from main.models import Experience, Project


# =========================
# AUTHORIZATION HELPER
# =========================

def is_editor(user):
    return (
        user.is_authenticated
        and user.groups.filter(name="Editor").exists()
    )


# =========================
# MAIN
# =========================

def show_main(request):
    last_login = request.COOKIES.get(
        "last_login",
        "Belum ada sesi login / Cookie tidak ditemukan"
    )

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
        "last_login": last_login,
    }

    return render(
        request,
        "index.html",
        context
    )


# =========================
# AUTHENTICATION
# =========================

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()

        messages.success(
            request,
            "Akun berhasil dibuat. Silakan login."
        )

        return redirect("main:login")

    context = {
        "name": "I Komang Arka Darma Laksana",
        "form": form,
    }

    return render(
        request,
        "register.html",
        context
    )


def login_user(request):
    form = AuthenticationForm(
        request,
        data=request.POST or None
    )

    if request.method == "POST" and form.is_valid():
        user = form.get_user()

        login(request, user)

        response = redirect("main:show_main")

        response.set_cookie(
            "last_login",
            timezone.localtime().strftime("%Y-%m-%d %H:%M:%S")
        )

        return response

    context = {
        "name": "I Komang Arka Darma Laksana",
        "form": form,
    }

    return render(
        request,
        "login.html",
        context
    )


def logout_user(request):
    logout(request)

    response = redirect("main:show_main")
    response.delete_cookie("last_login")

    return response


# =========================
# EXPERIENCE
# =========================

def show_experience(request):
    json_response = get_experience_json(request)

    experiences = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )

    experiences = [
        experience.object
        for experience in experiences
    ]

    context = {
        "name": "I Komang Arka Darma Laksana",
        "experience_list": experiences,
        "is_editor": is_editor(request.user),
    }

    return render(
        request,
        "experience.html",
        context
    )


def get_experience_json(request):
    experiences = Experience.objects.all()

    experiences_json = serializers.serialize(
        "json",
        experiences,
    )

    return HttpResponse(
        experiences_json,
        content_type="application/json",
    )


# =========================
# CREATE EXPERIENCE
# HANYA SUPERUSER
# =========================

@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    form = ExperienceForm(
        request.POST or None
    )

    if request.method == "POST" and form.is_valid():
        form.save()

        messages.success(
            request,
            "Experience baru berhasil ditambahkan!",
        )

        return redirect("main:show_experience")

    context = {
        "name": "I Komang Arka Darma Laksana",
        "form": form,
    }

    return render(
        request,
        "experience_form.html",
        context
    )


# =========================
# UPDATE EXPERIENCE
# SUPERUSER / EDITOR
# =========================

@login_required(login_url="/login/")
def update_experience(request, experience_id):
    experience = get_object_or_404(
        Experience,
        pk=experience_id,
    )

    if (
        not request.user.is_superuser
        and not is_editor(request.user)
    ):
        raise PermissionDenied

    form = ExperienceForm(
        request.POST or None,
        instance=experience,
    )

    if request.method == "POST" and form.is_valid():
        form.save()

        messages.success(
            request,
            "Experience berhasil diperbarui!",
        )

        return redirect("main:show_experience")

    context = {
        "name": "I Komang Arka Darma Laksana",
        "form": form,
        "experience": experience,
    }

    return render(
        request,
        "experience_form.html",
        context
    )


# =========================
# DELETE EXPERIENCE
# HANYA SUPERUSER
# =========================

@login_required(login_url="/login/")
def delete_experience(request, experience_id):
    experience = get_object_or_404(
        Experience,
        pk=experience_id,
    )

    if not request.user.is_superuser:
        raise PermissionDenied

    if request.method == "POST":
        experience.delete()

        messages.success(
            request,
            "Experience berhasil dihapus!",
        )

    return redirect(
        "main:show_experience"
    )


# =========================
# PROJECT
# =========================

def show_projects(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )

    projects = [
        project.object
        for project in projects
    ]

    name_query = request.GET.get(
        "name",
        ""
    ).strip()

    context = {
        "name": "I Komang Arka Darma Laksana",
        "project_list": projects,
        "name_query": name_query,
        "is_editor": is_editor(request.user),
    }

    return render(
        request,
        "projects.html",
        context
    )


# =========================
# CREATE PROJECT
# HANYA SUPERUSER
# =========================

@login_required(login_url="/login/")
def create_project(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    form = ProjectForm(
        request.POST or None
    )

    if request.method == "POST" and form.is_valid():
        form.save()

        messages.success(
            request,
            "Proyek baru berhasil ditambahkan!",
        )

        return redirect(
            "main:show_projects"
        )

    context = {
        "name": "I Komang Arka Darma Laksana",
        "form": form,
    }

    return render(
        request,
        "projects_form.html",
        context
    )


# =========================
# UPDATE PROJECT
# SUPERUSER / EDITOR
# =========================

@login_required(login_url="/login/")
def update_project(request, project_id):
    project = get_object_or_404(
        Project,
        pk=project_id,
    )

    if (
        not request.user.is_superuser
        and not is_editor(request.user)
    ):
        raise PermissionDenied

    form = ProjectForm(
        request.POST or None,
        instance=project,
    )

    if request.method == "POST" and form.is_valid():
        form.save()

        messages.success(
            request,
            "Project berhasil diperbarui!",
        )

        return redirect(
            "main:show_projects"
        )

    context = {
        "name": "I Komang Arka Darma Laksana",
        "form": form,
        "project": project,
    }

    return render(
        request,
        "projects_form.html",
        context
    )


# =========================
# STAR / UNSTAR
# USER YANG SUDAH LOGIN
# =========================

@login_required(login_url="/login/")
def toggle_star(request, project_id):
    project = get_object_or_404(
        Project,
        pk=project_id,
    )

    if request.method == "POST":
        if request.user in project.starred_by.all():
            project.starred_by.remove(
                request.user
            )
        else:
            project.starred_by.add(
                request.user
            )

    return redirect(
        "main:show_projects"
    )


# =========================
# PROJECT JSON API
# TIDAK MEMBOCORKAN STARRED_BY
# =========================

def get_projects_json(request):
    name_query = request.GET.get(
        "name",
        ""
    ).strip()

    projects = Project.objects.all()

    if name_query:
        projects = projects.filter(
            name__icontains=name_query
        )

    projects_json = serializers.serialize(
        "json",
        projects,
        fields=[
            "name",
            "description",
            "technology",
            "project_url",
            "project_image_url",
        ],
    )

    return HttpResponse(
        projects_json,
        content_type="application/json",
    )


# =========================
# DELETE PROJECT
# HANYA SUPERUSER
# =========================

@login_required(login_url="/login/")
def delete_project(request, project_id):
    project = get_object_or_404(
        Project,
        pk=project_id,
    )

    if not request.user.is_superuser:
        raise PermissionDenied

    if request.method == "POST":
        project.delete()

        messages.success(
            request,
            "Project berhasil dihapus!",
        )

        return redirect(
            "main:show_projects"
        )

    return redirect(
        "main:show_projects"
    )