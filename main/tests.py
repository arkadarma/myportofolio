from django.contrib.auth.models import Group, User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience, Project


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time",
        )

        self.project = Project.objects.create(
            name="Portfolio Website",
            description="Personal portfolio website using Django.",
            technology="Django",
        )

        # User biasa
        self.normal_user = User.objects.create_user(
            username="normaluser",
            password="testpass123",
        )

        # Editor
        self.editor_user = User.objects.create_user(
            username="editoruser",
            password="testpass123",
        )

        self.editor_group = Group.objects.create(
            name="Editor"
        )

        self.editor_user.groups.add(
            self.editor_group
        )

        # Superuser / owner
        self.superuser = User.objects.create_superuser(
            username="adminuser",
            password="testpass123",
            email="admin@example.com",
        )

    # =========================
    # MAIN
    # =========================

    def test_main_url_is_accessible(self):
        response = self.client.get(
            reverse("main:show_main")
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "index.html"
        )
        self.assertNotContains(
            response,
            self.experience.title
        )
        self.assertContains(
            response,
            f'href="{reverse("main:show_experience")}"'
        )

    def test_nonexistent_page_returns_404(self):
        response = self.client.get(
            "/halaman-yang-tidak-ada/"
        )

        self.assertEqual(
            response.status_code,
            404
        )

    # =========================
    # EXPERIENCE MODEL
    # =========================

    def test_experience_model(self):
        self.assertEqual(
            str(self.experience),
            "Asisten Dosen PBP"
        )
        self.assertEqual(
            self.experience.category,
            "part-time"
        )
        self.assertTrue(
            self.experience.is_ongoing
        )

    # =========================
    # EXPERIENCE PAGE
    # =========================

    def test_experience_page(self):
        response = self.client.get(
            reverse("main:show_experience")
        )

        self.assertEqual(
            response.status_code,
            200
        )
        self.assertTemplateUsed(
            response,
            "experience.html"
        )
        self.assertContains(
            response,
            self.experience.title
        )
        self.assertContains(
            response,
            self.experience.description
        )
        self.assertContains(
            response,
            "Part-Time"
        )
        self.assertContains(
            response,
            "Sedang berlangsung"
        )
        self.assertContains(
            response,
            f'href="{reverse("main:show_main")}"'
        )

    def test_empty_experience_page(self):
        Experience.objects.all().delete()

        response = self.client.get(
            reverse("main:show_experience")
        )

        self.assertContains(
            response,
            "Belum ada pengalaman yang ditambahkan."
        )

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()

        response = self.client.get(
            reverse("main:show_experience")
        )

        self.assertFalse(
            self.experience.is_ongoing
        )
        self.assertContains(
            response,
            "Selesai"
        )
        self.assertNotContains(
            response,
            "Sedang berlangsung"
        )

    # =========================
    # EXPERIENCE AUTHORIZATION
    # =========================

    def test_normal_user_cannot_create_experience(self):
        self.client.login(
            username="normaluser",
            password="testpass123"
        )

        response = self.client.get(
            reverse("main:create_experience")
        )

        self.assertEqual(
            response.status_code,
            403
        )

    def test_normal_user_cannot_update_experience(self):
        self.client.login(
            username="normaluser",
            password="testpass123"
        )

        response = self.client.get(
            reverse(
                "main:update_experience",
                args=[self.experience.id]
            )
        )

        self.assertEqual(
            response.status_code,
            403
        )

    def test_normal_user_cannot_delete_experience(self):
        self.client.login(
            username="normaluser",
            password="testpass123"
        )

        response = self.client.get(
            reverse(
                "main:delete_experience",
                args=[self.experience.id]
            )
        )

        self.assertEqual(
            response.status_code,
            403
        )

    def test_editor_can_update_experience(self):
        self.client.login(
            username="editoruser",
            password="testpass123"
        )

        response = self.client.get(
            reverse(
                "main:update_experience",
                args=[self.experience.id]
            )
        )

        self.assertEqual(
            response.status_code,
            200
        )

    def test_editor_cannot_create_experience(self):
        self.client.login(
            username="editoruser",
            password="testpass123"
        )

        response = self.client.get(
            reverse("main:create_experience")
        )

        self.assertEqual(
            response.status_code,
            403
        )

    # =========================
    # PROJECT PAGE
    # =========================

    def test_project_url_is_accessible(self):
        response = self.client.get(
            reverse("main:show_projects")
        )

        self.assertEqual(
            response.status_code,
            200
        )
        self.assertTemplateUsed(
            response,
            "projects.html"
        )

    def test_project_data_is_displayed(self):
        response = self.client.get(
            reverse("main:show_projects")
        )

        self.assertContains(
            response,
            self.project.name
        )
        self.assertContains(
            response,
            self.project.description
        )
        self.assertContains(
            response,
            self.project.technology
        )

    def test_empty_project_page(self):
        Project.objects.all().delete()

        response = self.client.get(
            reverse("main:show_projects")
        )

        self.assertContains(
            response,
            "Belum ada proyek yang ditambahkan."
        )

    # =========================
    # PROJECT AUTHORIZATION
    # =========================

    def test_normal_user_cannot_create_project(self):
        self.client.login(
            username="normaluser",
            password="testpass123"
        )

        response = self.client.get(
            reverse("main:create_project")
        )

        self.assertEqual(
            response.status_code,
            403
        )

    def test_normal_user_cannot_update_project(self):
        self.client.login(
            username="normaluser",
            password="testpass123"
        )

        response = self.client.get(
            reverse(
                "main:update_project",
                args=[self.project.id]
            )
        )

        self.assertEqual(
            response.status_code,
            403
        )

    def test_normal_user_cannot_delete_project(self):
        self.client.login(
            username="normaluser",
            password="testpass123"
        )

        response = self.client.get(
            reverse(
                "main:delete_project",
                args=[self.project.id]
            )
        )

        self.assertEqual(
            response.status_code,
            403
        )

    def test_editor_can_update_project(self):
        self.client.login(
            username="editoruser",
            password="testpass123"
        )

        response = self.client.get(
            reverse(
                "main:update_project",
                args=[self.project.id]
            )
        )

        self.assertEqual(
            response.status_code,
            200
        )

    def test_editor_cannot_create_project(self):
        self.client.login(
            username="editoruser",
            password="testpass123"
        )

        response = self.client.get(
            reverse("main:create_project")
        )

        self.assertEqual(
            response.status_code,
            403
        )

    def test_editor_cannot_delete_project(self):
        self.client.login(
            username="editoruser",
            password="testpass123"
        )

        response = self.client.get(
            reverse(
                "main:delete_project",
                args=[self.project.id]
            )
        )

        self.assertEqual(
            response.status_code,
            403
        )

    # =========================
    # GUEST AUTHORIZATION
    # =========================

    def test_guest_is_redirected_to_login_for_project_edit(self):
        response = self.client.get(
            reverse(
                "main:update_project",
                args=[self.project.id]
            )
        )

        self.assertEqual(
            response.status_code,
            302
        )

        self.assertIn(
            "/login/",
            response.url
        )

    def test_guest_is_redirected_to_login_for_project_create(self):
        response = self.client.get(
            reverse("main:create_project")
        )

        self.assertEqual(
            response.status_code,
            302
        )

        self.assertIn(
            "/login/",
            response.url
        )

    # =========================
    # STAR
    # =========================

    def test_normal_user_can_star_project(self):
        self.client.login(
            username="normaluser",
            password="testpass123"
        )

        response = self.client.post(
            reverse(
                "main:toggle_star",
                args=[self.project.id]
            )
        )

        self.assertEqual(
            response.status_code,
            302
        )

        self.assertTrue(
            self.project.starred_by.filter(
                id=self.normal_user.id
            ).exists()
        )

    def test_normal_user_can_unstar_project(self):
        self.client.login(
            username="normaluser",
            password="testpass123"
        )

        self.project.starred_by.add(
            self.normal_user
        )

        response = self.client.post(
            reverse(
                "main:toggle_star",
                args=[self.project.id]
            )
        )

        self.assertEqual(
            response.status_code,
            302
        )

        self.assertFalse(
            self.project.starred_by.filter(
                id=self.normal_user.id
            ).exists()
        )

    def test_guest_cannot_star_project(self):
        response = self.client.post(
            reverse(
                "main:toggle_star",
                args=[self.project.id]
            )
        )

        self.assertEqual(
            response.status_code,
            302
        )

        self.assertIn(
            "/login/",
            response.url
        )

    def test_star_count(self):
        self.project.starred_by.add(
            self.normal_user,
            self.editor_user,
        )

        self.assertEqual(
            self.project.starred_by.count(),
            2
        )

    # =========================
    # PROJECT JSON API
    # =========================

    def test_project_json_api_is_accessible(self):
        response = self.client.get(
            reverse("main:get_projects_json")
        )

        self.assertEqual(
            response.status_code,
            200
        )

        self.assertEqual(
            response["Content-Type"],
            "application/json"
        )

    def test_project_json_does_not_expose_starred_by(self):
        self.project.starred_by.add(
            self.normal_user
        )

        response = self.client.get(
            reverse("main:get_projects_json")
        )

        content = response.content.decode(
            "utf-8"
        )

        self.assertNotIn(
            "starred_by",
            content
        )

        self.assertNotIn(
            self.normal_user.username,
            content
        )