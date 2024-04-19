# Generated by Django 3.2.25 on 2024-04-19 16:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('username', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('bio', models.TextField(null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Male', max_length=6)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('last_edited_at', models.DateTimeField(auto_now=True)),
                ('avatar', models.ImageField(default='avatar.svg', null=True, upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('title', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('url', models.URLField()),
                ('platform', models.CharField(choices=[('Codechef', 'Codechef'), ('Leetcode', 'Leetcode'), ('Codeforces', 'Codeforces')], max_length=10)),
                ('start_time', models.DateTimeField()),
                ('duration', models.DurationField()),
                ('total_questions', models.IntegerField(null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_edited_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DevToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('url', models.URLField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('platform', models.CharField(choices=[('Codechef', 'Codechef'), ('Leetcode', 'Leetcode'), ('Codeforces', 'Codeforces')], max_length=10)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_edited_at', models.DateTimeField(auto_now=True)),
                ('submitted_by', models.ManyToManyField(blank=True, related_name='problemstouser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('submission_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('submitted_at', models.DateTimeField(null=True)),
                ('submission_link', models.URLField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_edited_at', models.DateTimeField(auto_now=True)),
                ('problem', models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='base.problem')),
                ('submitted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('host', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('participants', models.ManyToManyField(blank=True, related_name='participants', to=settings.AUTH_USER_MODEL)),
                ('topic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.topic')),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
        migrations.CreateModel(
            name='RatingChange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating_change', models.IntegerField()),
                ('final_rating', models.IntegerField()),
                ('time_taken', models.DurationField(null=True)),
                ('rank', models.IntegerField()),
                ('number_of_problems_solved', models.IntegerField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_edited_at', models.DateTimeField(auto_now=True)),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.contest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
        migrations.CreateModel(
            name='Leetcode',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('rating', models.IntegerField(null=True)),
                ('global_rank', models.IntegerField(null=True)),
                ('number_of_contests', models.IntegerField(null=True)),
                ('number_of_questions', models.IntegerField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LeetcodeToUser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Codeforces',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('rating', models.IntegerField(null=True)),
                ('global_rank', models.IntegerField(null=True)),
                ('number_of_contests', models.IntegerField(null=True)),
                ('number_of_questions', models.IntegerField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CodeforcesToUser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Codechef',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('rating', models.IntegerField(null=True)),
                ('global_rank', models.IntegerField(null=True)),
                ('number_of_contests', models.IntegerField(null=True)),
                ('number_of_questions', models.IntegerField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CodechefToUser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='codechef',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='CodechefToUser', to='base.codechef'),
        ),
        migrations.AddField(
            model_name='user',
            name='codeforces',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='CodeforcesToUser', to='base.codeforces'),
        ),
        migrations.AddField(
            model_name='user',
            name='leetcode',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='LeetcodeToUser', to='base.leetcode'),
        ),
    ]
