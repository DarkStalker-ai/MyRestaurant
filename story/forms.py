from django import forms

class CheckoutForm(forms.Form):
    PAYMENT_CHOICES = [
        ('online', 'Онлайн'),
        ('cash', 'Готівка'),
    ]

    full_name = forms.CharField(label='Повне ім\'я', max_length=100)
    phone = forms.CharField(label='Телефон', max_length=20)
    address = forms.CharField(label='Адреса доставки', max_length=200)
    payment_method = forms.ChoiceField(label='Спосіб оплати', choices=PAYMENT_CHOICES)
