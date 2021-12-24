from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.TextField()),
                ('userName', models.TextField()),
                ('profile_url', models.TextField()),
                ('email', models.TextField()),
                ('description', models.TextField()),
                ('pPhoto', models.TextField()),
                ('createDate',models.TextField()),
                ('blog', models.TextField()),
                ('company', models.TextField()),
                ('location',models.TextField()),
                ('reposName', models.TextField()),
                ('reposLanguages', models.TextField()),

            ],
        ),
    ]
