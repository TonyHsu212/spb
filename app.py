#name: weimin xu
#studentID: 1159079

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
import re
from datetime import datetime
import mysql.connector
from mysql.connector import FieldType
import connect
from admin_interface import administrator_api

app = Flask(__name__)

dbconn = None
connection = None
admin_api = administrator_api()


def getCursor():
    global dbconn
    global connection
    connection = mysql.connector.connect(user=connect.dbuser, \
    password=connect.dbpass, host=connect.dbhost, \
    database=connect.dbname, autocommit=True)
    dbconn = connection.cursor()
    return dbconn


@app.route("/")
def home():
    return render_template('homemenu.html')

@app.route("/currentjobs")
def currentjobs():
    # connection = getCursor()
    # connection.execute("SELECT job_id,customer,job_date FROM job where completed=0;")
    # jobList = connection.fetchall()
    jobList = []
    return render_template("currentjoblist.html", job_list = jobList)    

@app.route("/admin")
def to_admin():
    return render_template("admin.html")

@app.route("/technician")
def to_technician():
    return render_template("technician.html")


# @app.route("/customer_list", methods=['post'])
# def list_resutl():
#     if request.method == "POST":
#         resutl = request.form.to_dict()
#         b = admin()
#         b.getresutl(resutl)
#         return render_template('customer_list.html', num1 = 'successful')


@app.route("/customer_list")
def tolist_allcustomer_information():
    connection = getCursor()
    customerlist = admin_api.tolist_allcustomer(connection)
    connection.close()
    return render_template("customer_list.html",customerlist = customerlist)


@app.route("/toadd_customer", methods=["POST", "GET"])
def toadd_customer():
    connection = getCursor()
    if request.method == 'POST':
        result = request.form.to_dict()

    # admin_api.getresutl(result)
    id = admin_api.get_next_customerid(connection)
    connection.execute("insert into customer values (%s,%s,%s,%s,%s)", (id,result['first_name'], result['family_name'],result['customer_email'],result['customer_phone']))

    return render_template("admin.html", result='****Successfully')


@app.route("/tosearch_customer_id", methods=["POST", "GET"])
def tosearch_customer_id():
    connection = getCursor()
    if request.method == 'POST':
        customer_id = request.form.to_dict()
        id = customer_id['customer_id']

    # customerlist = admin_api.customers_search(id, connection)
    connection.execute("SELECT * FROM customer where customer_id = %s;", (id,))
    customerlist = connection.fetchall()
    return render_template('customer_list.html', customerlist = customerlist)

@app.route("/tosearch_customer_name", methods=["POST", "GET"])
def tosearch_customer_name():
    connection = getCursor()
    if request.method == "GET":
        render_template('admin.html')

    if request.method == 'POST':
        customer_name = request.form.to_dict()
        customer_name = customer_name['customer_name']

    # customerlist = admin_api.customers_search(id, connection)
    connection.execute("SELECT * FROM customer where first_name = %s or family_name = %s;", (customer_name, customer_name, ))
    customerlist = connection.fetchall()
    return render_template('customer_list.html', customerlist = customerlist)


@app.route("/toadd_newservices_system", methods=['post', 'get'])
def toadd_newservices_system():
    connection = getCursor()
    if request.method == 'POST':
        result = request.form.to_dict()

    print(result['new_service_cost'])
    print(result['new_service_name'])
    # admin_api.getresutl(result)
    id = admin_api.get_next_serviceid(connection)
    print(id)
    connection.execute("insert into service values (%s,%s,%s)", (id, result['new_service_name'], result['new_service_cost']))

    return render_template("admin.html", result='****Successfully')


@app.route("/customer_list")
def toadd_newparts_system():
    return render_template('customer_list.html')

@app.route("/customer_list")
def toschedule_job_jobid():
    return render_template('customer_list.html')

@app.route("/customer_list")
def toschedule_job_customerid():
    return render_template('customer_list.html')

@app.route("/customer_list")
def toschedule_job_customername():
    return render_template('customer_list.html')


@app.route("/customer_list")
def tocheck_paycondition_jobid():
    return render_template('customer_list.html')

@app.route("/customer_list")
def tocheck_paycondition_customerid():
    return render_template('customer_list.html')

@app.route("/customer_list")
def tocheck_paycondition_customername():
    return render_template('customer_list.html')












if __name__ == '__main__':
    app.run()

