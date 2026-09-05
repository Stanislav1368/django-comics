import json

from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from .data import COMICS, UI_TEXT
from .forms import ReaderPreferencesForm

COOKIE_MAX_AGE = 60 * 60 * 24 * 180


def get_preferences(request: HttpRequest) -> dict[str, str]:
    """Read and validate the visitor's preferences from cookies."""
    theme = request.COOKIES.get("reader_theme", "paper")
    font_size = request.COOKIES.get("reader_font_size", "medium")
    language = request.COOKIES.get("reader_language", "ru")

    if theme not in {"paper", "night", "neon"}:
        theme = "paper"
    if font_size not in {"small", "medium", "large"}:
        font_size = "medium"
    if language not in UI_TEXT:
        language = "ru"

    return {"theme": theme, "font_size": font_size, "language": language}


def base_context(request: HttpRequest) -> dict:
    preferences = get_preferences(request)
    return {
        **preferences,
        "ui": UI_TEXT[preferences["language"]],
    }


def home(request: HttpRequest) -> HttpResponse:
    context = base_context(request)
    last_read = request.COOKIES.get("last_read")
    context["comics"] = COMICS
    context["last_comic"] = next(
        (comic for comic in COMICS if comic["slug"] == last_read),
        None,
    )
    return render(request, "comics/home.html", context)


def reader(request: HttpRequest, slug: str) -> HttpResponse:
    comic = next((item for item in COMICS if item["slug"] == slug), None)
    if comic is None:
        raise Http404("Такого выпуска нет в библиотеке.")

    context = base_context(request)
    language = context["language"]
    context["comic"] = comic
    context["comic_title"] = comic["title_en"] if language == "en" else comic["title"]
    context["comic_description"] = (
        comic["description_en"] if language == "en" else comic["description"]
    )

    response = render(request, "comics/reader.html", context)
    response.set_cookie("last_read", slug, max_age=COOKIE_MAX_AGE, samesite="Lax")

    visited = request.COOKIES.get("visited_comics", "[]")
    try:
        visited_slugs = json.loads(visited)
        if not isinstance(visited_slugs, list):
            visited_slugs = []
    except json.JSONDecodeError:
        visited_slugs = []
    visited_slugs = [slug] + [item for item in visited_slugs if item != slug]
    response.set_cookie(
        "visited_comics",
        json.dumps(visited_slugs[:5]),
        max_age=COOKIE_MAX_AGE,
        samesite="Lax",
    )
    return response


def preferences(request: HttpRequest) -> HttpResponse:
    context = base_context(request)
    if request.method == "POST":
        form = ReaderPreferencesForm(request.POST)
        if form.is_valid():
            response = redirect("comics:home")
            response.set_cookie(
                "reader_theme",
                form.cleaned_data["theme"],
                max_age=COOKIE_MAX_AGE,
                samesite="Lax",
            )
            response.set_cookie(
                "reader_font_size",
                form.cleaned_data["font_size"],
                max_age=COOKIE_MAX_AGE,
                samesite="Lax",
            )
            response.set_cookie(
                "reader_language",
                form.cleaned_data["language"],
                max_age=COOKIE_MAX_AGE,
                samesite="Lax",
            )
            return response
    else:
        form = ReaderPreferencesForm(
            initial={
                "theme": context["theme"],
                "font_size": context["font_size"],
                "language": context["language"],
            }
        )

    context["form"] = form
    return render(request, "comics/settings.html", context)
