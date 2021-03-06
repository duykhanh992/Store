# Generated by Django 3.0.8 on 2020-07-28 22:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Carrier',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('phone_no', models.CharField(max_length=255)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=255)),
                ('added_on', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerRequest',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('prod_details', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=False)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('joining_date', models.DateField()),
                ('phone', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('buy_price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('sell_price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('in_stock_total', models.IntegerField()),
                ('qty_in_strip', models.IntegerField()),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('carrier_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Carrier')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('salt_name', models.CharField(max_length=255)),
                ('salt_qty', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('add_on', models.DateTimeField(auto_now_add=True)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeSalary',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('salary_date', models.DateField()),
                ('salary_amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeBank',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bank_account_no', models.CharField(max_length=255)),
                ('ifsc_no', models.CharField(max_length=255)),
                ('added_on', models.DateTimeField()),
                ('empoloyee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='CarrierBank',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bank_account_no', models.CharField(max_length=255)),
                ('ifsc_no', models.CharField(max_length=255)),
                ('added_on', models.DateField(auto_now_add=True)),
                ('Carrier_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Carrier')),
            ],
        ),
        migrations.CreateModel(
            name='CarrierAccount',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('transaction_type', models.CharField(choices=[(1, 'Debit'), (2, 'Credit'), (3, 'VND')], max_length=255)),
                ('transaction_amt', models.CharField(max_length=255)),
                ('transaction_date', models.DateField()),
                ('payment_mode', models.CharField(max_length=255)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('carrier_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Carrier')),
            ],
        ),
        migrations.CreateModel(
            name='BillDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('qty', models.IntegerField()),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('bill_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Bill')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
            ],
        ),
        migrations.AddField(
            model_name='bill',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Customer'),
        ),
    ]
