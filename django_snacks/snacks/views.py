from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomepageView(TemplateView):
  template_name = 'home.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['snacks'] = [
      {
        "image_url": "https://www.kelloggs.com/content/dam/NorthAmerica/kelloggs/en_US/images/Brandlogo/Frosted-Mini-Wheats-Logo_349x208.png",
        "title": "Frosted Mini-Wheats",
        "description": "Frosted Mini-Wheats® Original are made to help fill you up with 10 layers of whole shredded wheat in every delicious bite. Just 1 bowl, and you are good till lunch!",
        "reference_url": "https://www.kelloggs.com/en_US/brands/frosted-mini-wheats-consumer-brand.html"
      }, {
        "image_url": "https://images.kglobalservices.com/www.kelloggs.com/en_us/product/product_4508497/prod_img-3394699_new_redbox_optimized.png",
        "title": "Froot Loops",
        "description": "Bursting with flavor and a delicious crunch Froot Loops® Cereal is the fruitiest way to start your day.",
        "reference_url": "https://www.kelloggs.com/en_US/products/froot-loops-cereal.html"
      }, {
        "image_url": "https://images.kglobalservices.com/www.kelloggs.com/en_us/product/product_9425438/prod_img-10546356_prod_img-10546356.png",
        "title": "Little Debbie® Oatmeal Creme Pies Cereal",
        "description": "Classic oatmeal cookie aroma, spices and notes of creme, introducing Little Debbie® Oatmeal Creme Pies Cereal! Get a spoonful of timeless taste and cinnamon flavor.",
        "reference_url": "https://www.kelloggs.com/en_US/products/licensed-cereal-oatmeal-cream-pie.html"
      }, 
    ]

    return context

class AboutView(TemplateView):
  template_name = 'about.html'
