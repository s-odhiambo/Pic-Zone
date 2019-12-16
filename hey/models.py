from django.db import models

class Location(models.Model):
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.location


    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category

    def save_category(self):
        self.save()

    @classmethod
    def get_all_categories(cls):
        categ = cls.objects.all()
        return categ

    @classmethod
    def delete_category(cls,category):
        cls.objects.filter(category=category).delete()
        

class Image(models.Model):
    title =models.CharField(max_length =60)
    post_date = models.DateTimeField(auto_now_add=True)
    location_item=models.ForeignKey('Location',on_delete=models.CASCADE,)
    category_item=models.ForeignKey('Category',on_delete=models.CASCADE,)
    image = models.ImageField(upload_to ='images/')
    
    @classmethod
    def display_all(cls):
        display=cls.objects.all()
        return display

    def __str__(self):
        return self.title

    def save_image(self):
        self.save()

    @classmethod 
    def search_by_category(cls,search_term):
        images= cls.objects.filter(category_item__category__icontains=search_term)
        return images
    
    
    
    
    