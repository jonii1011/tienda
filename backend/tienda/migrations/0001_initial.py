# Generated by Django 5.1.3 on 2024-12-07 04:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id_carrito', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FormaDePago',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id_modelo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_modelo', models.CharField(max_length=100)),
                ('version', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TipoProducto',
            fields=[
                ('id_tipo_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_tipo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='productos/')),
                ('modelo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tienda.modelo')),
                ('tipo_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.tipoproducto')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleCarrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='tienda.carrito')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles_carrito', to='tienda.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dni', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('fecha_de_nacimiento', models.DateField(blank=True, null=True)),
                ('direccion', models.CharField(blank=True, max_length=255, null=True)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('rol', models.CharField(choices=[('cliente', 'Cliente'), ('administrador', 'Administrador')], default='cliente', max_length=50)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to.', related_name='usuario_set', related_query_name='usuario', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='usuario_set', related_query_name='usuario', to='auth.permission')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='carrito',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.usuario'),
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id_venta', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_venta', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.usuario')),
                ('forma_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.formadepago')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.producto')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='tienda.venta')),
            ],
        ),
    ]
