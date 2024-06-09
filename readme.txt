pyinstaller -F -i logo.ico ask_GUI.py
pip freeze > requirements.txt
pip install -r requirements.txt