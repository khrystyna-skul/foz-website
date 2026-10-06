from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [('foz_website', '0002_exchangeprogram')]
    operations = [
        migrations.RunSQL(
            sql="""
            INSERT INTO foz_website_exchangeprogram (university, languages, places, deadline, description) VALUES
            ('Uniwersytet Warszawski, Польща', 'польська, англійська', '5', '2026-11-15', 'Один із найстаріших і найпрестижніших університетів Польщі.'),
            ('KU Leuven (Бельгія)', 'English', '2 місця', '2026-12-01', 'Провідний дослідницький університет Бельгії з багатою історією.'),
            ('Vilnius University, Литва', 'англійська', 'до 4', '2026-10-20', 'Найстаріший університет у Балтійських країнах.'),
            ('Uniwersytet Jagielloński, Польща', 'Польська, Англійська', '3', '2026-11-15', 'Один із найдавніших вищих навчальних закладів у Центральній Європі.'),
            ('University of Tartu - Естонія', 'англійська, естонська', '2', '2027-01-10', 'Провідний центр вищої освіти та наукових досліджень в Естонії.'),
            ('Masaryk University, Чехія', 'англійська', '1 місце', '2026-09-30', 'Другий за величиною університет Чеської Республіки.');
            """,
            reverse_sql="DELETE FROM foz_website_exchangeprogram;"
        )
    ]