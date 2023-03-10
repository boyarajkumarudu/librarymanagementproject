# Generated by Django 4.1.4 on 2023-01-25 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BOOk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Book_name', models.CharField(max_length=60)),
                ('Author_name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_name', models.CharField(max_length=60)),
                ('Student_phone', models.BigIntegerField()),
                ('Student_sem', models.IntegerField()),
                ('Student_pswd', models.CharField(max_length=60)),
                ('Student_Course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryapp.course')),
            ],
        ),
        migrations.CreateModel(
            name='Issue_Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Start_date', models.DateField()),
                ('Start_end', models.DateField()),
                ('S_Book_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryapp.book')),
                ('S_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryapp.student')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='Course_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryapp.course'),
        ),
    ]
