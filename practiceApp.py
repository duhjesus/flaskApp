from flask import Flask, render_template #tells flask to use template
#flask app
app = Flask(__name__) #name= name of file as it stands in current import tree
#allows flask to identify this app variable as something specific

#identify route or endpt, what users type when they arrive on our app
@app.route('/') #python decorator defines function directly below
def home():     #url or endpt here is / function home runs
    #test = "Hello World" #www.mysite.com/ (doesnt care about domain www.mysite.com just end pt /)
    #return test
    return render_template('home.html')

#last thing to do is to run app
app.run()

#now run in terminal
