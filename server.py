from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')

@app.route('/')
def index():
    print "Hello from server! This is base route"
    friends = mysql.query_db("SELECT myfriends.name, myfriends.age, DATE_FORMAT(myfriends.created_at, '%M %D %Y') AS friends_since FROM myfriends")
    #friends = mysql.query_db("SELECT * FROM myfriends")
    print friends[0]
    return render_template('friends.html', myfriends=friends)

@app.route('/addfriend', methods=['POST'])
def create():
    # add a friend to the database!
    # Write query as a string. Notice how we have multiple values
    # we want to insert into our query.
    query = "INSERT INTO myfriends (name, age, created_at, updated_at) VALUES (:name, :age, NOW(), NOW())"
    # We'll then create a dictionary of data from the POST data received.
    data = {
             'name': request.form['name'],
             'age':  request.form['age'],
           }
    # Run query, with dictionary values injected into the query.
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)