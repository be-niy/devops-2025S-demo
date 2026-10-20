from django.test import TestCase
from django.urls import reverse


class AdminAccessTests(TestCase):
    def test_anonymous_user_is_redirected_to_admin_login(self):
        admin_url = reverse("admin:index")
        login_url = reverse("admin:login")

        response = self.client.get(admin_url)

        self.assertRedirects(
            response,
            f"{login_url}?next={admin_url}",
            fetch_redirect_response=False,
        )# Create your tests here.
