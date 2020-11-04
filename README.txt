# TheBusyBeavers
CS361 - Ethical Eating

INITIAL SETUP

- set up virtual environment on flip, in folder of your choice 
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
- Run Flask Persistently
      gunicorn run:app -b 0.0.0.0:#### -D
