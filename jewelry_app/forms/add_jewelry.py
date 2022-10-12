from django import forms
from jewelry_app.models import Jewelry


class AddJewelry(forms.Form):
    name = forms.CharField(
        label="Ad - Soyad",
        max_length=50,
        required=True,
        error_messages={
            "required": "Lütfen takı takacağınız kişinin ismini girin .",
            "max_length": "Lütfen 50 Karakteri aşmayın",
        },
        disabled=False,
        widget=forms.TextInput(
            attrs={
                "class": "special",
                "size": "18",
                "title": "Ad - Soyad",
                "required": True
            }
        )
    )
    price = forms.IntegerField(label="Miktar")
    CHOICES = (
        (1, "Gram Altın"),
        (2, "Çeyrek Altın"),
        (3, "Yarım Altın"),
        (4, "Tam Altın"),
        (5, "Cumhuriyet Altını"),
        (6, "Dolar"),
        (7, "Euro"),
        (8, "Türk Lirası"),
    )

    jewelry_kind = forms.ChoiceField(label="Takı Türü", choices=CHOICES)
