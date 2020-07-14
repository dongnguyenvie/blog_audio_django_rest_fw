# SCRAPY COMMANDS
scrapy-stack:
	cd scrapping && scrapy crawl stack

scrapy-shell:
	cd scrapping && scrapy shell

# DJANGO COMMANDS
django-run:
	cd djangoapp && ./manage.py runserver

django-migrations:
	cd djangoapp && ./manage.py makemigrations

django-migrate:
	cd djangoapp && ./manage.py migrate

django-static:
	cd djangoapp && ./manage.py collectstatic