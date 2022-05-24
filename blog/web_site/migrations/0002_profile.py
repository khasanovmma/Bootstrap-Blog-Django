
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web_site', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(default='About me')),
                ('profile_image', models.ImageField(blank=True, upload_to='photo/profile')),
                ('website_url', models.CharField(max_length=255)),
                ('github_url', models.CharField(max_length=255)),
                ('instagram_url', models.CharField(max_length=255)),
                ('facebook_url', models.CharField(max_length=255)),
                ('telegram_url', models.CharField(max_length=255)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
