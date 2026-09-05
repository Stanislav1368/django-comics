from django import forms


class ReaderPreferencesForm(forms.Form):
    """Form for the reading preferences saved in browser cookies."""

    THEME_CHOICES = [
        ("paper", "Бумага / Paper"),
        ("night", "Ночь / Night"),
        ("neon", "Неон / Neon"),
    ]
    FONT_CHOICES = [
        ("small", "Маленький / Small"),
        ("medium", "Средний / Medium"),
        ("large", "Большой / Large"),
    ]
    LANGUAGE_CHOICES = [
        ("ru", "Русский"),
        ("en", "English"),
    ]

    theme = forms.ChoiceField(
        choices=THEME_CHOICES,
        widget=forms.RadioSelect,
        label="Тема",
    )
    font_size = forms.ChoiceField(
        choices=FONT_CHOICES,
        widget=forms.RadioSelect,
        label="Размер текста",
    )
    language = forms.ChoiceField(
        choices=LANGUAGE_CHOICES,
        widget=forms.RadioSelect,
        label="Язык интерфейса",
    )
