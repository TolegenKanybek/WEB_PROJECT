from django.db import migrations, models





class Migration(migrations.Migration):



    dependencies = [

        ('api', '0001_initial'),

    ]



    operations = [

        migrations.AddField(

            model_name='category',

            name='description',

            field=models.TextField(default=''),

        ),

    ]