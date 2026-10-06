import re
from django.db import migrations


def split_data(apps, schema_editor):
    ExchangeProgram = apps.get_model('foz_website', 'ExchangeProgram')

    data_map = [
        ('Uniwersytet Warszawski', 'Польща'),
        ('KU Leuven', 'Бельгія'),
        ('Vilnius University', 'Литва'),
        ('Uniwersytet Jagielloński', 'Польща'),
        ('University of Tartu', 'Естонія'),
        ('Masaryk University', 'Чехія'),
    ]
    programs = list(ExchangeProgram.objects.all().order_by('id'))
    for idx, prog in enumerate(programs):
        if idx < len(data_map):
            prog.university_name = data_map[idx][0]
            prog.country = data_map[idx][1]
            if hasattr(prog, 'university'):
                prog.university = f"{data_map[idx][0]}, {data_map[idx][1]}"
            prog.save()


def reverse_split_data(apps, schema_editor):
    ExchangeProgram = apps.get_model('foz_website', 'ExchangeProgram')
    for prog in ExchangeProgram.objects.all():
        if hasattr(prog, 'university'):
            u_name = getattr(prog, 'university_name', '')
            c_name = getattr(prog, 'country', '')
            if u_name and c_name:
                prog.university = f"{u_name}, {c_name}"
            elif u_name:
                prog.university = u_name
            prog.save()


class Migration(migrations.Migration):
    dependencies = [
        ('foz_website', '0004_split_university_country_schema'),
    ]

    operations = [
        migrations.RunPython(split_data, reverse_code=reverse_split_data),
    ]