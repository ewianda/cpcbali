#!/usr/bin/env bash
rm db.sqlite3
./manage.py syncdb --noinput
./manage.py loaddata app/fixtures/*
echo "from django.contrib.auth import get_user_model;  User=get_user_model(); User.objects.create_superuser('wiandaelvis@gmail.com', 'love')" | ./manage.py shell
