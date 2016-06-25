# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-25 16:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import parler.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.CharField(help_text='app id, identical to folder name', max_length=128, primary_key=True, serialize=False, unique=True, verbose_name='Id')),
                ('user_docs', models.URLField(blank=True, max_length=256, verbose_name='User documentation url')),
                ('admin_docs', models.URLField(blank=True, max_length=256, verbose_name='Admin documentation url')),
                ('developer_docs', models.URLField(blank=True, max_length=256, verbose_name='Developer documentation url')),
                ('issue_tracker', models.URLField(blank=True, max_length=256, verbose_name='Issue tracker url')),
                ('website', models.URLField(blank=True, max_length=256, verbose_name='Homepage')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('featured', models.BooleanField(default=False, verbose_name='Featured')),
            ],
            options={
                'verbose_name_plural': 'Apps',
                'verbose_name': 'App',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='AppRelease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(help_text='Version follows Semantic Versioning', max_length=128, verbose_name='Version')),
                ('php_version_spec', models.CharField(max_length=128, verbose_name='PHP version requirement')),
                ('platform_version_spec', models.CharField(max_length=128, verbose_name='Platform version requirement')),
                ('min_int_size', models.IntegerField(blank=True, default=32, help_text='e.g. 32 for 32bit Integers', verbose_name='Minimum Integer Bits')),
                ('checksum', models.CharField(max_length=64, verbose_name='SHA256 checksum')),
                ('download', models.URLField(blank=True, max_length=256, verbose_name='Archive download Url')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='releases', to='core.App', verbose_name='App')),
            ],
            options={
                'verbose_name_plural': 'App Releases',
                'verbose_name': 'App Release',
                'ordering': ['-version'],
            },
        ),
        migrations.CreateModel(
            name='AppTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(help_text='Rendered app name for users', max_length=128, verbose_name='Name')),
                ('description', models.TextField(help_text='Will be rendered as Markdown', verbose_name='Description')),
                ('master', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='core.App')),
            ],
            options={
                'db_tablespace': '',
                'managed': True,
                'verbose_name': 'App Translation',
                'db_table': 'core_app_translation',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.CharField(help_text='Category id which is used to identify a category. Used to identify categories when uploading an app', max_length=128, primary_key=True, serialize=False, unique=True, verbose_name='Id')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'verbose_name': 'Category',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CategoryTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(help_text='Category name which will be presented to the user', max_length=128, verbose_name='Name')),
                ('description', models.TextField(help_text='Will be rendered as Markdown', verbose_name='Description')),
                ('master', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='core.Category')),
            ],
            options={
                'db_tablespace': '',
                'managed': True,
                'verbose_name': 'Category Translation',
                'db_table': 'core_category_translation',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Database',
            fields=[
                ('id', models.CharField(help_text='Key which is used to identify a database', max_length=128, primary_key=True, serialize=False, unique=True, verbose_name='Id')),
                ('name', models.CharField(help_text='Database name which will be presented to the user', max_length=128, verbose_name='Name')),
            ],
            options={
                'verbose_name_plural': 'Databases',
                'verbose_name': 'Database',
            },
        ),
        migrations.CreateModel(
            name='DatabaseDependency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_spec', models.CharField(max_length=128, verbose_name='Database version requirement')),
                ('app_release', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='databasedependencies', to='core.AppRelease', verbose_name='App release')),
                ('database', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='releasedependencies', to='core.Database', verbose_name='Database')),
            ],
            options={
                'verbose_name_plural': 'Database Dependencies',
                'verbose_name': 'Database Dependency',
            },
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.CharField(help_text='Key which is used to identify a license', max_length=128, primary_key=True, serialize=False, unique=True, verbose_name='Id')),
                ('name', models.CharField(help_text='License name which will be presented to the user', max_length=128, verbose_name='Name')),
            ],
            options={
                'verbose_name_plural': 'Licenses',
                'verbose_name': 'License',
            },
        ),
        migrations.CreateModel(
            name='PhpExtension',
            fields=[
                ('id', models.CharField(help_text='e.g. libxml', max_length=128, primary_key=True, serialize=False, unique=True, verbose_name='PHP extension')),
            ],
            options={
                'verbose_name_plural': 'PHP Extensions',
                'verbose_name': 'PHP Extension',
            },
        ),
        migrations.CreateModel(
            name='PhpExtensionDependency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_spec', models.CharField(max_length=128, verbose_name='Extension version requirement')),
                ('app_release', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phpextensiondependencies', to='core.AppRelease', verbose_name='App Release')),
                ('php_extension', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='releasedependencies', to='core.PhpExtension', verbose_name='PHP Extension')),
            ],
            options={
                'verbose_name_plural': 'PHP Extension Dependencies',
                'verbose_name': 'PHP Extension Dependency',
            },
        ),
        migrations.CreateModel(
            name='Screenshot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=256, verbose_name='Image url')),
                ('ordering', models.IntegerField(verbose_name='Ordering')),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='screenshots', to='core.App', verbose_name='App')),
            ],
            options={
                'verbose_name_plural': 'Screenshots',
                'verbose_name': 'Screenshot',
                'ordering': ['ordering'],
            },
        ),
        migrations.CreateModel(
            name='ShellCommand',
            fields=[
                ('name', models.CharField(help_text='Name of a required shell command, e.g. grep', max_length=128, primary_key=True, serialize=False, unique=True, verbose_name='Shell Command')),
            ],
            options={
                'verbose_name_plural': 'Shell Commands',
                'verbose_name': 'Shell Command',
            },
        ),
        migrations.AddField(
            model_name='apprelease',
            name='databases',
            field=models.ManyToManyField(blank=True, through='core.DatabaseDependency', to='core.Database', verbose_name='Database dependency'),
        ),
        migrations.AddField(
            model_name='apprelease',
            name='licenses',
            field=models.ManyToManyField(to='core.License', verbose_name='License'),
        ),
        migrations.AddField(
            model_name='apprelease',
            name='php_extensions',
            field=models.ManyToManyField(blank=True, through='core.PhpExtensionDependency', to='core.PhpExtension', verbose_name='PHP extension dependency'),
        ),
        migrations.AddField(
            model_name='apprelease',
            name='shell_commands',
            field=models.ManyToManyField(blank=True, to='core.ShellCommand', verbose_name='Shell command dependency'),
        ),
        migrations.AddField(
            model_name='app',
            name='categories',
            field=models.ManyToManyField(to='core.Category', verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='app',
            name='co_maintainers',
            field=models.ManyToManyField(blank=True, related_name='co_maintained_apps', to=settings.AUTH_USER_MODEL, verbose_name='Co-Maintainers'),
        ),
        migrations.AddField(
            model_name='app',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_apps', to=settings.AUTH_USER_MODEL, verbose_name='App owner'),
        ),
        migrations.AddField(
            model_name='app',
            name='recommendations',
            field=models.ManyToManyField(blank=True, related_name='recommended_apps', to=settings.AUTH_USER_MODEL, verbose_name='Recommendations'),
        ),
        migrations.AlterUniqueTogether(
            name='phpextensiondependency',
            unique_together=set([('app_release', 'php_extension', 'version_spec')]),
        ),
        migrations.AlterUniqueTogether(
            name='databasedependency',
            unique_together=set([('app_release', 'database', 'version_spec')]),
        ),
        migrations.AlterUniqueTogether(
            name='categorytranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='apptranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='apprelease',
            unique_together=set([('app', 'version')]),
        ),
    ]
