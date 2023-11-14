# Generated by Django 4.2.7 on 2023-11-09 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_blog_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='PassportInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveSmallIntegerField(verbose_name='Yoshi')),
                ('seria', models.CharField(max_length=2)),
                ('num', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterModelOptions(
            name='author',
            options={},
        ),
        migrations.RemoveField(
            model_name='author',
            name='age',
        ),
        migrations.RemoveField(
            model_name='author',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='author',
            name='lastname',
        ),
        migrations.AddField(
            model_name='author',
            name='status',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Menager', 'Menager'), ('super_admin', 'super_admin')], default='Menager', max_length=12),
        ),
        migrations.AddField(
            model_name='author',
            name='info',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.passportinfo', verbose_name='Pasport ma`lumotlari'),
        ),
    ]
