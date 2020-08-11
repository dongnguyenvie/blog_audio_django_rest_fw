import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':  os.getenv("POSTGRES_DB_NAME", "audiovyvy_prod"),
        'USER': os.getenv("POSTGRES_USER", "root"),
        'PASSWORD': os.getenv("POSTGRES_PASS", ""),
        'HOST': os.getenv("POSTGRES_HOST", ""),
        'PORT': os.getenv("POSTGRES_PORT", ""),
    }
}
