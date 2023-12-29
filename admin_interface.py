#name: weimin xu
#studentID: 1159079
from flask import Flask, render_template
from werkzeug.datastructures import ImmutableDict

app = Flask(__name__)

class administrator_api:
    #Display a list of customers, ordered by surname, then by first name.
    # def tolist_customer(self):
    #     pass
    def __init__(self):
        return None

    def __del__(self):
        return None

    def tolist_customer1(self):
        return 4

    def tolist_allcustomer(self, connection):
       # connection = getCursor()
       connection.execute("SELECT * FROM customer;")
       customerlist = connection.fetchall()

       return customerlist

    #Search for customers by first name or surname, allowing for partial text matches. Order the results appropriately.
    def customers_search(customer_id, connection):
        connection.execute("SELECT * FROM customer where customer_id = %s;", (id,))
        customerlist = connection.fetchall()
        return customerlist

    def customers_search1(customer_name):
        pass

    #Add a new customer to the system (surname, phone number and email address are required fields)
    def add_customers(id, customer_name):
        pass

    #Add a new service to the system (name and cost are required)
    def add_newservices_system(id, services_id, cost):
        pass

    #Add a new part to the system (name and cost are required)
    def add_newparts_system(id, parts_id, cost):
        pass

    #Select a customer and a date for the job to be booked for.
    # The date must be today or in the future. Only the date is required
    # – a time on that day is not required.
    def schedule_job(job_id):
        pass

    def schedule_job(customer_id):
        pass

    #Shows all unpaid bills in date then customer order, which can be filtered by customer.
    # A bill can then be selected so that it can be marked as paid by the Admin.
    # Bills that are paid should not show on the list.
    def unpaidbills_or_payedbills(customer_id):
        pass

    def unpaidbills_or_payedbills(customer_name):
        pass

    def unpaidbills_or_payedbills(job_id):
        pass

    # A report showing all bills that,
    # with bills that are unpaid more than 14 days after the date of the job highlighted in red.
    # The display should include the customer details, the date of the job,
    # the total cost of the job. Bills should be grouped by customer,
    # so that the customer details are only shown once above the list of bills for that customer.
    # Customers should be shown in last name, first name order. Bills should be shown with the oldest bill first.
    def billing_history(customer_id):
        pass

    def billing_history(customer_name):
        pass

    def billing_history(job_id):
        pass

    def billing_overdue(customer_id):
        pass

    def billing_overdue(job_id):
        pass

    def billing_overdue(customer_name):
        pass

    def getresutl(self, x):
        # print(x)
        pass

    def get_next_customerid(self, connection):
        connection.execute('select max(customer_id) from customer;')
        id = connection.fetchall()
        id = id[0][0] + 1
        return id

    def get_next_serviceid(self, connection):
        connection.execute('select max(service_id) from service;')
        id = connection.fetchall()
        id = id[0][0] + 1
        return id
