from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            "name",
            "description",
            "technology",
            "project_image_url",
        ]

        labels = {
            "name": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "technology": "Teknologi yang Digunakan",
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
            "project_image_url": forms.URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...",
                }
            ),
        }