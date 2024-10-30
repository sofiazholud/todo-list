##TODO List Project
This is a simple web application for managing a to-do list, built with Django.

#Features
Tasks: Users can add, update, delete, and mark tasks as completed.
Tags: Each task can be assigned tags to organize tasks by category.

#Installation
1.Clone the repository:

git clone <your-repository-url>
cd todo-list

2.Set up a virtual environment:

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

3.Install dependencies:

pip install -r requirements.txt

4.Apply migrations:

python manage.py makemigrations
python manage.py migrate

5.Create a superuser (optional):

python manage.py createsuperuser

6.Start the server:

python manage.py runserver

#Usage
Home Page: Shows the list of all tasks.
Tags Page: Allows categorization of tasks using tags.

#License
This project is licensed under the MIT License.