from flask import Flask, render_template 

app = Flask(__name__)
cloudy = {
    'name': "Cloud Aggregator", #static name
    'clouds':{ #dynamic
        1:{
            'cloud_id': 1,
            'title': 'First cloud storage',
            'content': 'Hello world!'
        }
    } 
}


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/cloud/<int:cloud_id>')#go to specific endpt /cloud/2 for example
def cloud(cloud_id):
    cloudService = cloudy['clouds'][cloud_id]
    return render_template('cloud.jinja2',template_variable=cloudService)#keyword argument in python and w/ render_template allows a template to access variable inside the template called cloudService

app.run()