from django.db import migrations, connection

def create_enrollments_table(apps, schema_editor):
    with connection.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS enrollments (
                enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(50) NOT NULL,
                course_id INT NOT NULL,
                enrolled_at DATETIME
            )
        """)

def drop_enrollments_table(apps, schema_editor):
    with connection.cursor() as cursor:
        cursor.execute("DROP TABLE IF EXISTS enrollments")

class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_enrollments_table, reverse_code=drop_enrollments_table),
    ]