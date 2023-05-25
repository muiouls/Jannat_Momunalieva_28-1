from django import forms
from posts.models import Review, Product


class ProductCreateForm(forms.Form):
    image = forms.FileField(required=False)
    title = forms.CharField(max_length=256)
    description = forms.CharField(widget=forms.Textarea())
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    quantity = forms.IntegerField()


class ReviewCreateForm(forms.Form):
    text = forms.CharField(max_length=256)
    product = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].choices = [(product.id, product.title) for product in Product.objects.all()]
