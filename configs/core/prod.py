print('MODE IS production')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'audiovyvy_prod',
        'USER': 'root',
        'PASSWORD': 'Abc@123',
        'HOST': 'pi-ubuntu1.local',
        'PORT': '5432',
    }
}
