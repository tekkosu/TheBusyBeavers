# TheBusyBeavers
CS361 - Ethical Eating

INITIAL SETUP

- set up virtual environment on flip, in folder of your choice (don't set it up in the same folder as the Ethical Eats github folder)
      bash 
      virtualenv venv -p $(which python3)
- activate your virtual env
      source ./venv/bin/activate
	
- Install Flask
      pip3 install --upgrade pip
      pip3 install flask
      pip3 install gunicorn
		
- Set Flask_App environment variable and debug (while in virtual environment)
      export FLASK_APP=run.py
      export FLASK_DEBUG=1
- Run Flask
      python -m flask run -h 0.0.0.0 -p #### (replace #### with port number)
- Or Run Flask Persistently
      gunicorn run:app -b 0.0.0.0:#### -D

Resources:
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
https://getbootstrap.com/docs/4.0/components/navbar/
