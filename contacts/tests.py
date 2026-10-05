from urllib.parse import urlencode

from django.db import models
from django.test import Client, TestCase
from django.urls import reverse

from .models import Contact


class ContactTests(TestCase):
    def setUp(self):
        self.contact = Contact.objects.create(
            name="Ani Lestari", email="ani@example.com"
        )

    def contact_url(self, name):
        return reverse(f"contacts:{name}", args=[self.contact.pk])

    def test_model_uses_integer_primary_key_and_name(self):
        self.assertIsInstance(Contact._meta.pk, models.AutoField)
        self.assertEqual(str(self.contact), "Ani Lestari")

    def test_list_renders_full_page_with_contact(self):
        response = self.client.get(reverse("contacts:contact_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contacts/index.html")
        self.assertContains(response, self.contact.name)
        self.assertContains(response, self.contact.email)
        self.assertContains(response, 'id="contact-rows"')

    def test_empty_list_renders_placeholder(self):
        Contact.objects.all().delete()
        response = self.client.get(reverse("contacts:contact_list"))
        self.assertContains(response, "Tidak ada kontak.")

    def test_add_creates_contact_and_returns_all_rows(self):
        response = self.client.post(
            reverse("contacts:contact_add"),
            {"name": "Budi Santoso", "email": "budi@example.com"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Contact.objects.filter(name="Budi Santoso").exists())
        self.assertTemplateUsed(response, "contacts/_contact_rows.html")
        self.assertContains(response, self.contact.name)
        self.assertContains(response, "Budi Santoso")
        self.assertNotContains(response, "<html")

    def test_search_filters_name_case_insensitively_and_clears(self):
        Contact.objects.create(name="Budi Santoso", email="budi@example.com")
        url = reverse("contacts:contact_search")
        response = self.client.get(url, {"q": "ANI"})
        self.assertContains(response, "Ani Lestari")
        self.assertNotContains(response, "Budi Santoso")
        self.assertNotContains(response, "<html")
        self.assertContains(self.client.get(url, {"q": ""}), "Budi Santoso")
        self.assertContains(self.client.get(url, {"q": "missing"}), "Tidak ada kontak.")

    def test_edit_inputs_are_associated_with_form_in_action_cell(self):
        response = self.client.get(self.contact_url("contact_edit"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contacts/_contact_edit_row.html")
        self.assertContains(response, f'form="edit-form-{self.contact.pk}"', count=2)
        self.assertContains(response, f'id="edit-form-{self.contact.pk}"')
        self.assertContains(response, f'value="{self.contact.name}"')
        self.assertNotContains(response, "<html")

    def test_put_updates_url_encoded_values_and_returns_display_row(self):
        response = self.client.put(
            self.contact_url("contact_update"),
            urlencode({"name": "Ani & Citra", "email": "ani+updated@example.com"}),
            content_type="application/x-www-form-urlencoded",
        )
        self.assertEqual(response.status_code, 200)
        self.contact.refresh_from_db()
        self.assertEqual(self.contact.name, "Ani & Citra")
        self.assertEqual(self.contact.email, "ani+updated@example.com")
        self.assertTemplateUsed(response, "contacts/_contact_row.html")
        self.assertContains(response, "Ani &amp; Citra")
        self.assertNotContains(response, "<form")

    def test_put_preserves_fields_not_in_request(self):
        self.client.put(
            self.contact_url("contact_update"),
            urlencode({"name": "Ani Updated"}),
            content_type="application/x-www-form-urlencoded",
        )
        self.contact.refresh_from_db()
        self.assertEqual(self.contact.name, "Ani Updated")
        self.assertEqual(self.contact.email, "ani@example.com")

    def test_cancel_returns_original_row_without_saving(self):
        self.client.get(self.contact_url("contact_edit"))
        response = self.client.get(
            self.contact_url("contact_row"), {"name": "Unsaved name"}
        )
        self.assertContains(response, "Ani Lestari")
        self.assertNotContains(response, "Unsaved name")
        self.contact.refresh_from_db()
        self.assertEqual(self.contact.name, "Ani Lestari")

    def test_delete_returns_empty_200_and_removes_contact(self):
        response = self.client.delete(self.contact_url("contact_delete"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"")
        self.assertFalse(Contact.objects.filter(pk=self.contact.pk).exists())

    def test_update_and_delete_reject_wrong_methods(self):
        self.assertEqual(
            self.client.post(self.contact_url("contact_update")).status_code, 405
        )
        self.assertEqual(
            self.client.get(self.contact_url("contact_delete")).status_code, 405
        )
        self.assertTrue(Contact.objects.filter(pk=self.contact.pk).exists())

    def test_missing_contact_returns_404(self):
        pk = self.contact.pk + 100
        for name, method in [
            ("contact_edit", "get"), ("contact_row", "get"),
            ("contact_update", "put"), ("contact_delete", "delete"),
        ]:
            with self.subTest(view=name):
                url = reverse(f"contacts:{name}", args=[pk])
                self.assertEqual(getattr(self.client, method)(url).status_code, 404)

    def test_csrf_required_for_post_put_and_delete(self):
        client = Client(enforce_csrf_checks=True)
        client.get(reverse("contacts:contact_list"))
        token = client.cookies["csrftoken"].value
        mutations = [
            ("post", reverse("contacts:contact_add")),
            ("put", self.contact_url("contact_update")),
            ("delete", self.contact_url("contact_delete")),
        ]
        for method, url in mutations:
            with self.subTest(method=method):
                self.assertEqual(getattr(client, method)(url).status_code, 403)

        headers = {"HTTP_X_CSRFTOKEN": token}
        response = client.post(
            reverse("contacts:contact_add"),
            {"name": "Citra", "email": "citra@example.com"}, **headers,
        )
        self.assertEqual(response.status_code, 200)
        response = client.put(
            self.contact_url("contact_update"),
            urlencode({"name": "Ani Updated", "email": "ani@example.com"}),
            content_type="application/x-www-form-urlencoded", **headers,
        )
        self.assertEqual(response.status_code, 200)
        self.contact.refresh_from_db()
        self.assertEqual(self.contact.name, "Ani Updated")
        self.assertEqual(
            client.delete(self.contact_url("contact_delete"), **headers).status_code,
            200,
        )
