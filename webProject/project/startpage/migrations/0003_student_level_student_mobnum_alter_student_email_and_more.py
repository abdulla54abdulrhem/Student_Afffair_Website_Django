# Generated by Django 4.0.4 on 2022-05-22 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startpage', '0002_student_email_student_gpa'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='level',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='mobNum',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='gpa',
            field=models.DecimalField(decimal_places=1, max_digits=1, null=True),
        ),
    ]
