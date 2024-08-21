from django.db import models

# Create your models here.

class Material(models.Model):
    material_id = models.AutoField(primary_key=True)
    materials = models.CharField(max_length=200, null=False, default=False)
    material_sub_type = models.CharField(max_length=50)
    thickness = models.DecimalField(max_digits=5, decimal_places=2, help_text="Thickness in mm", default=0.00)
    finish = models.CharField(max_length=50)
    length = models.DecimalField(max_digits=255, decimal_places=2, help_text="Length in mm", default=0.00)
    width = models.DecimalField(max_digits=255, decimal_places=2, help_text="Width in mm", default=0.00)
    cost = models.DecimalField(blank=False, null=False, max_digits=8, decimal_places=2, help_text="Cost in #", default=0.00, editable=False)
    vendor = models.CharField(max_length=200, null=False, default=False)



    def save(self, *args, **kwargs):
        self.cost = self.thickness * self.length * self.width 
        super().save(*args, **kwargs)

    def __str__(self):
        return self.cost