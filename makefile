ppr:
	git push origin faraji && gh pr create --web -B dev

dev:
	python manage.py makemigrations && python manage.py migrate && python manage.py runserver
	