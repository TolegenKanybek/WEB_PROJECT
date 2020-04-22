from django.db import migrations

class Migration(migrations.Migration):



    dependencies = [

        ('api', '0002_category_description'),

    ]



    operations = [

        migrations.RemoveField(

            model_name='category',

            name='description',

        ),

    ]