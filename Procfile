web: gunicorn vinta_teste.wsgi --chdir backend --limit-request-line 8188 --log-file -
worker: celery worker --workdir backend --app=vinta_teste -B --loglevel=info
