from multiprocessing import connection
from flask import Flask, render_template, url_for, json, redirect, request
# from flask import Flask, render_template, json, redirect
# from flask_mysqldb import MySQL
import os
import pymysql
from pymysql.cursors import DictCursor
# from dotenv import load_dotenv
app = Flask(__name__)

def mysql():
    # load_dotenv()
    host = 'x71wqc4m22j8e3ql.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
    database = 'qr4o0gbq7gjqofgs'
    username = 'p9n6cam78xno3vw6'
    password = "vnm82vo5d0ec601i"
    connection = pymysql.connect(host=host, user=username,
                           password=password, database=database, cursorclass=DictCursor)
    print(connection)
    return connection


listsMembers = [
  {
      "memberID": 1,
      "cycleID": 2,
      "email": "Ophelia.Murillo@us.af.mil"
  },
  {
      "memberID": 2,
      "cycleID": 6,
      "email": "Beau.Davie@us.af.mil"
  },
  {
      "memberID": 3,
      "cycleID": 1,
      "email": "Natasha.Fernandez@us.af.mil"
  },
  {
      "memberID": 4,
      "cycleID": 5,
      "email": "Ammar.Clegg@us.af.mil"
  },
  {
      "memberID": 5,
      "cycleID": 2,
      "email": "Usamah.Franco@us.af.mil"
  },
  {
      "memberID": 6,
      "cycleID": 8,
      "email": "Macaulay.Larsen@us.af.mil"
  }
]

listsAssignments = [
  {
      "assignmentID": 1,
      "commanderID": 1,
      "cycleID": 4,
      "location": "Ft Meade"
  },
  {
      "assignmentID": 2,
      "commanderID": 2,
      "cycleID": 2,
      "location": "Beale"
  },
  {
      "assignmentID": 3,
      "commanderID": 3,
      "cycleID": 4,
      "location": "Travis"
  },
    {
      "assignmentID": 4,
      "commanderID": 4,
      "cycleID": 7,
      "location": "Eglin"
  },
  {
      "assignmentID": 5,
      "commanderID": 5,
      "cycleID": 5,
      "location": "Wright-Patterson"
  },
  {
      "assignmentID": 6,
      "commanderID": 6,
      "cycleID": 1,
      "location": "Moody"
  }
]

listsCycles = [
  {
      "cycleID": 1,
      "season": "Summer",
      "year": 2022
  },
  {
      "cycleID": 2,
      "season": "Winter",
      "year": 2023
  },
  {
      "cycleID": 3,
      "season": "Summer",
      "year": 2023
  },
  {
      "cycleID": 4,
      "season": "Winter",
      "year": 2024
  },
  {
      "cycleID": 5,
      "season": "Summer",
      "year": 2024
  },
  {
      "cycleID": 6,
      "season": "Winter",
      "year": 2026
  },
]

listsCommanders = [
  {
      "commanderID": 1,
      "email": "Emily.Mackay@us.af.mil"
  },
  {
      "commanderID": 2,
      "email": "Anastasia.Clarkson@us.af.mil"
  },
  {
      "commanderID": 3,
      "email": "Inigo.Montoya@us.af.mil"
  },
  {
      "commanderID": 4,
      "email": "Paddy.Rangel@us.af.mil"
  },
  {
      "commanderID": 5,
      "email": "Finnian.Morgan@us.af.mil"
  },
  {
      "commanderID": 6,
      "email": "Leoni.Bernal@us.af.mil"
  },
]

listsBids = [
  {
      "bidID": 1,
      "assignmentID": 1,
      "memberID": 1,
      "bidByMember": "True",
      "bidByCommander": "False"
  },
  {
      "bidID": 2,
      "assignmentID": 7,
      "memberID": 8,
      "bidByMember": "True",
      "bidByCommander": "False"
  },
  {
      "bidID": 3,
      "assignmentID": 8,
      "memberID": 11,
      "bidByMember": "True",
      "bidByCommander": "True"
  },
  {
      "bidID": 4,
      "assignmentID": 13,
      "memberID": 12,
      "bidByMember": "False",
      "bidByCommander": "True"
  },
  {
      "bidID": 5,
      "assignmentID": 15,
      "memberID": 17,
      "bidByMember": "True",
      "bidByCommander": "False"
  },
  {
      "bidID": 6,
      "assignmentID": 16,
      "memberID": 20,
      "bidByMember": "True",
      "bidByCommander": "True"
  }
]

@app.route('/')
def root():
    return render_template("main.j2")

# @app.route('/members', methods=["POST", "GET"], endpoint='members')
# def root():
#     return render_template("members.j2", listsMembers=listsMembers)

@app.route('/members', methods=["POST", "GET"])
def Members():
    # insert a member into the bids entity
    if request.method == "POST":
        # fire off if user presses the Add Member button
        if request.form.get("Add_Member"):
            # grab user form inputs
            cycleID = request.form["cycleID"]
            email = request.form["email"]

            query = "INSERT INTO Members (cycleID, email) VALUES (%s, %s)"
            connection = mysql()
            cursor = connection.cursor()        
            cursor.execute(query, (cycleID, email))
            connection.commit()
            cursor.close()
            connection.close()
            return redirect("/members")

    if request.method == "GET":
        # https://stackoverflow.com/questions/9845102/using-mysql-in-flask
        query = "SELECT * FROM Members"
        connection = mysql()
        cursor = connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()
        connection.close()
        return render_template("members.j2", data=data)


# route for edit functionality, updating the attributes of a member in Members
# similar to our delete route, we want to the pass the 'id' value of that member on button click (see HTML) via the route
@app.route("/edit_members/<int:id>", methods=["POST", "GET"])
def edit_members(id):
    if request.method == "GET":
        # mySQL query to grab the info of the member with our passed id
        query = "SELECT * FROM Members WHERE id = %s" % (id)
        connection = mysql()
        cursor = connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()
        connection.close()

        # render edit_members page passing our query data to the edit_members template
        return render_template("edit_members.j2", data=data)

    # meat and potatoes of our update functionality
    if request.method == "POST":
        # fire off if user clicks the 'Edit Member' button
        if request.form.get("Edit_Member"):
            # grab user form inputs
            memberID = request.form["memberID"]
            cycleID = request.form["cycleID"]
            email = request.form["email"]

            # no null inputs
            query = "UPDATE Members SET Members.cycleID = %s, Members.email = %s WHERE Members.memberID = %s"
            connection = mysql()
            cursor = connection.cursor()        
            cursor.execute(query, (cycleID, email, memberID))
            connection.commit()
            cursor.close()
            connection.close()
  
            # redirect back to members page after we execute the update query
            return redirect("/members")

@app.route('/assignments/', methods=['GET'], endpoint='assignments')
def assignments():

  return render_template("assignments.j2", listsAssignments=listsAssignments)

@app.route('/bids/', methods=['GET'], endpoint='bids')
def bids():
  return render_template("bids.j2", listsBids=listsBids)

@app.route('/commanders/', methods=['GET'], endpoint='commanders')
def commanders():
  return render_template("commanders.j2", listsCommanders=listsCommanders)

@app.route('/cycles/',methods=['GET'], endpoint='cycles')
def cycles():
  return render_template("cycles.j2", listsCycles=listsCycles)


if __name__ == "__main__":
    app.run()