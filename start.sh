#!/bin/bash
echo "Making migrations..."
python /app/manage.py makemigrations

echo "Aplying migrations..."
python /app/manage.py migrate

echo "Creating superuser..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@rdvl.net', 'admin')
    print("Superuser created")
else:
    print("Superuser already exists")
EOF

echo "Starting Django server..."
python /app/manage.py runserver 0.0.0.0:8000