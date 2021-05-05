# TopTrends
> Django-based news generator web application

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This is web application that leverages the news API to generate news from multiple sources.
	
## Technologies
Project is created with:
* Python version 3.8.7
* Django verion 3.1.6
* Bootstrap version 4
* HTML
* CSS

## Setup


1. Git Clone the project with: ```git clone https://github.com/HenryOchieng/TopTrends.git```.

2. Move to the base directory: ```cd TopTrends```

3. Create a new python enveronment with: ```python -m venv env```.

4. Activate enveronment with: ```env\Scripts\activate``` on windows, or ```source env/bin/activate``` on Mac and Linux.

5. Install required dependences with: ```pip install -r requirements.txt```.

6. Make migrations with: ```python manage.py makemigrations``` and then ```python manage.py migrate```.

7. Run app localy with: ```python manage.py runserver```.
