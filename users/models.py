from django.db import models



class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    company = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, unique=True, null=False)
    phone_number = models.CharField(max_length=12)
    design_file = models.FileField(upload_to='design_files/', null=True, blank=True)  # To store uploaded files
    is_catalog = models.BooleanField(default=False)  # To distinguish catalog items
    created_at = models.DateTimeField(auto_now_add=True)
    user_type = models.CharField(choices=[('admin', 'Admin'), ('general_user', 'General User')], default='general_user')


    def __str__(self):
        return self.user.name
    

    






