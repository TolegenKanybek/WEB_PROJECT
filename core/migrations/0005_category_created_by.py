from django.conf import settings

from django.db import migrations, models

import django.db.models.deletion





class Migration(migrations.Migration):



    dependencies = [

        migrations.swappable_dependency(settings.AUTH_USER_MODEL),

        ('api', '0004_product'),

    ]



    operations = [

        migrations.AddField(

            model_name='category',

            name='created_by',

            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),

        ),

    ]