# quiz
Sample Code Quiz Application

# Assumptions

- Default templating language and the default Django ORM are being left in place since there appears to be an emphasis on using vanilla python + Django.

- Quiz application will consist of the following components:
  * Instructional Content
  * Quiz Question
  * Lesson - grouping logic between instructional content and quiz questions
    * A listing page for all available lessons.
    * A view page to view the lesson + quiz questions.
    * A score page for viewing your score for that quiz.

- Not included for expediency:
  * Logged in users / saved scores / session tracking. Except for users created for use with the admin.
  * Using SQLite

# How to run locally

  * inside a virtualenv run: pip install -r requirements.txt
  * run: python manage.py migrate
  * run: python manage.py createsuperuser
  * run: python manage.py runserver
  * navigate in a browswer to: http://127.0.0.1:8000/ or http://127.0.0.1:8000/admin
  

