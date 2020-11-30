gunicorn --log-file - --worker-tmp-dir /dev/shm --workers 8 --bind 0.0.0.0:8000 --graceful-timeout 300 --timeout 540 --enable-stdio-inheritance --capture-output quantum_common.wsgi:application
