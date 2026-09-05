from django.test import Client, TestCase
from django.urls import reverse


class ComicReaderTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_page_contains_comic_collection(self):
        response = self.client.get(reverse("comics:home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Звёздный пилот")

    def test_reader_sets_last_read_cookie(self):
        response = self.client.get(reverse("comics:reader", kwargs={"slug": "tea-witch"}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.cookies["last_read"].value, "tea-witch")

    def test_settings_are_saved_in_cookies(self):
        response = self.client.post(
            reverse("comics:preferences"),
            {"theme": "night", "font_size": "large", "language": "en"},
        )
        self.assertRedirects(response, reverse("comics:home"))
        self.assertEqual(response.cookies["reader_theme"].value, "night")
        self.assertEqual(response.cookies["reader_font_size"].value, "large")
        self.assertEqual(response.cookies["reader_language"].value, "en")

    def test_unknown_comic_returns_404(self):
        response = self.client.get(reverse("comics:reader", kwargs={"slug": "missing"}))
        self.assertEqual(response.status_code, 404)
