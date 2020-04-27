# flaskApp
Purpose: developing web App with flask/python or at the very least exploring this as a viable option.

single python file and few html/jinja files(flask template language which
allows user to give some content or page to display)

flask is python web framework( maps urls to python functions)
-show page, check user login, display data.
python 3.6
display some html content, allow users to submit form( very important in web app)
save things to inmemory database(not persistenting things to disk,so not available between running sessions, dictionary)

simple blog app.

1. virtualenv will be used instead of venv ( using older python versions)
2. app.py
   i. defining what are flask app does
   ii. what the endpoints are( thing user can type in browser are)
   iii. what we are going to do when the user types something in the browser
3. use app.py to create hello world 
4. go to terminal to run, make sure source activate script is on
5. python app.py go to browser with terminal output url link
6. now create html webpage and display it using flask
7. create "templates" directory(has to be named that), where html/ginger will be here
8. give html file to users using route / and import render_template func from Flask library
9. flask app running with html content being served is done. next step have web app store posts
10. users given currently avaiable posts and are allowed to make new posts.

###### basics learned from:
Youtuber "Udemy Tech"'s guide as a starting point to building an app w/ flask.
