from django.db import migrations, models

import django.db.models.deletion





class Migration(migrations.Migration):



    dependencies = [

        ('api', '0003_remove_category_description'),

    ]



    operations = [

        migrations.CreateModel(

            name='Product',

            fields=[

                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),

                ('name', models.CharField(max_length=200)),

                ('price', models.FloatField()),

                ('count', models.IntegerField()),

                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Category')),

            ],

        ),

    ]