#!/bin/sh
sleep 10
php artisan migrate
php artisan serve --port=8000 --host=0.0.0.0
