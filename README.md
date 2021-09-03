# BlogCreator

<img src="" width=35 height=25> 
- A website where we can create and share beautiful blogs with anyone, this website is created with respect to industry standards

## :desktop_computer:	Installation

### :hammer_and_wrench: Requirements
* Python 3.6+
* Django 3.0+
* Django-ckeditor
* Django-bottstrap4
* Pillow

##### NOTE: Use requirements.txt file for easy installations

## :gear: Setting up encironment for project

1. Create a Environment using below Command
```
$ conda create -n YourEnvName python=3.6
```

2. Activate Your Environment
```
$ conda activate EnvName
```

3. Install All Requirenments using requirements.txt

NOTE: goto to the folder when requirements.txt file is present before executing the below command.

```
$ pip freeze > requirements.txt
```

4. Configure the project

NOTE: Make sure you are in the main project folder
```
$ python manage.py migrate
```

```
$ python manage.py makemigrations
```

```
$ python manage.py migrate
```

5. Run the Project on your Local System

```
$ pthon manage.py runserver
```

## Contributors <img src="https://raw.githubusercontent.com/TheDudeThatCode/TheDudeThatCode/master/Assets/Developer.gif" width=35 height=25> 

- Suraj Jaiswal