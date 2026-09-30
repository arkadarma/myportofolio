from django import forms
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags

from .models import Project, Experience


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            "name",
            "description",
            "technology",
            "project_url",
            "project_image_url",
        ]

        labels = {
            "name": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "technology": "Teknologi yang Digunakan",
            "project_url": "URL Proyek",
            "project_image_url": "URL Gambar Proyek",
        }

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "placeholder": "Ceritakan Proyekmu",
                    "rows": 3,
                }
            ),
            "technology": forms.TextInput(
                attrs={
                    "placeholder": "Django, Python, HTML, CSS",
                }
            ),
            "project_url": forms.URLInput(
                attrs={
                    "placeholder": "https://github.com/username/project",
                }
            ),
            "project_image_url": forms.URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...",
                }
            ),
        }

    def clean_name(self):
        name = strip_tags(
            self.cleaned_data["name"]
        ).strip()

        if not name:
            raise ValidationError(
                "Nama proyek tidak boleh hanya berisi tag HTML."
            )

        return name

    def clean_technology(self):
        return strip_tags(
            self.cleaned_data["technology"]
        ).strip()

    def clean_description(self):
        return strip_tags(
            self.cleaned_data["description"]
        ).strip()


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
            "thumbnail",
            "ended_at",
        ]

        labels = {
            "title": "Judul Pengalaman",
            "description": "Deskripsi Pengalaman",
            "category": "Kategori",
            "thumbnail": "URL Thumbnail",
            "ended_at": "Tanggal Selesai",
        }

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "placeholder": "Software Engineer Intern",
                    "maxlength": 255,
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "placeholder": "Ceritakan pengalamanmu",
                    "rows": 4,
                }
            ),
            "category": forms.Select(
                attrs={
                    "style": (
                        "width: 100%;"
                        "min-height: 50px;"
                        "padding: 0.85rem 3rem 0.85rem 1rem;"
                        "border: 1px solid #63e6ff;"
                        "border-radius: 14px;"
                        "background-color: #0d111b;"
                        "color: #f5f7fb;"
                        "font-family: inherit;"
                        "font-size: 1rem;"
                        "cursor: pointer;"
                    )
                }
            ),
            "thumbnail": forms.URLInput(
                attrs={
                    "placeholder": "https://example.com/image.jpg",
                }
            ),
            "ended_at": forms.DateTimeInput(
                attrs={
                    "type": "datetime-local",
                }
            ),
        }

    def clean_title(self):
        title = strip_tags(
            self.cleaned_data["title"]
        ).strip()

        if not title:
            raise ValidationError(
                "Judul pengalaman tidak boleh hanya berisi tag HTML."
            )

        return title

    def clean_description(self):
        return strip_tags(
            self.cleaned_data["description"]
        ).strip()

    def clean_category(self):
        return strip_tags(
            self.cleaned_data["category"]
        ).strip()