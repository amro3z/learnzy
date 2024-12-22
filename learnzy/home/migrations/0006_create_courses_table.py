from django.db import migrations, connection

def create_courses_table(apps, schema_editor):
    with connection.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS courses (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(200) NOT NULL,
                description TEXT,
                instructor_id INT NOT NULL,
                video_url VARCHAR(255),
                image VARCHAR(100),
                created_at DATETIME,
                FOREIGN KEY (instructor_id) REFERENCES auth_user(id)
            )
        """)

def drop_courses_table(apps, schema_editor):
    with connection.cursor() as cursor:
        cursor.execute("DROP TABLE IF EXISTS courses")

class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_courses_table, reverse_code=drop_courses_table),
    ]