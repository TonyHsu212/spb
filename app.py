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
from technician_interface import techician_api
import bootstrap4

app = Flask(__name__)

dbconn = None
connection = None
admin_api = administrator_api()
tech_api = techician_api()

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
    connection.close()
    return render_template("admin.html", result1='****Successfully')


@app.route("/tosearch_customer_id", methods=["POST", "GET"])
def tosearch_customer_id():
    connection = getCursor()
    if request.method == 'POST':
        customer_id = request.form.to_dict()
        id = customer_id['customer_id']

    # customerlist = admin_api.customers_search(id, connection)
    connection.execute("SELECT * FROM customer where customer_id = %s;", (id,))
    customerlist = connection.fetchall()
    connection.close()
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
    connection.close()
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
    connection.close()
    return render_template("admin.html", result2='****Successfully')


@app.route("/toadd_newparts_system", methods=['post', 'get'])
def toadd_newparts_system():
    connection = getCursor()
    if request.method == 'POST':
        result = request.form.to_dict()

    print(result['new_part_cost'])
    print(result['new_part_name'])
    # admin_api.getresutl(result)
    id = admin_api.get_next_partid(connection)
    print(id)
    connection.execute("insert into part values (%s,%s,%s)", (id, result['new_part_name'], result['new_part_cost']))
    connection.close()
    return render_template("admin.html", result3='****Successfully')


@app.route("/toschedule_job_jobid", methods=['post', 'get'])
def toschedule_job_jobid():
    connection = getCursor()
    if request.method == 'POST':
        result = request.form.to_dict()

    print(result['schedule_job_jobid'])
    print(result['toschedule_job_jobdate'])
    # admin_api.getresutl(result)
    id = admin_api.get_next_jobid(connection)
    print(id)
    connection.execute("update job set job_date = (%s) where job_id = (%s)", (result['toschedule_job_jobdate'],result['schedule_job_jobid'],))
    connection.close()
    return render_template("admin.html", result4='****Successfully')


@app.route("/toschedule_job_customerid", methods=['post', 'get'])
def toschedule_job_customerid():
    connection = getCursor()
    if request.method == 'POST':
        result = request.form.to_dict()

    # print(result['schedule_job_customerid'])
    # print(result['schedule_job_due_date'])
    connection.execute("update job set job_date = (%s) where customer = (%s)", (result['schedule_job_due_date'],result['schedule_job_customerid'],))
    connection.close()
    return render_template("admin.html", result5='****Successfully')



@app.route("/tocheck_paycondition")
def tocheck_paycondition():
    connection = getCursor()
    customerlist = admin_api.tocheck_paycondition(connection)

    connection.close()
    return render_template('payout_status.html', customerlist = customerlist, str1='list all customers payout status')

@app.route("/toview_paymenthistory")
def toview_paymenthistory():
    connection = getCursor()
    customerlist = admin_api.toview_paymenthistory(connection)

    connection.close()
    return render_template('payout_status.html', customerlist = customerlist, str2='list all customers payout history')

@app.route("/toadd_services")
def add_services():
    connection = getCursor()
    if request.method == 'POST':
        result = request.form.to_dict()

    # admin_api.getresutl(result)
    id = tech_api.get_next_jobid(connection)
    connection.execute("insert into job values (%s,%s,%s,%s,%s)", (id,result['first_name'], result['family_name'],result['cost'],result['quant']))
    connection.close()
    return render_template("admin.html", result1='****Successfully')



if __name__ == '__main__':
    app.run()

