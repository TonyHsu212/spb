#name: weimin xu
#studentID: 1159079
from flask import Flask, render_template
from werkzeug.datastructures import ImmutableDict
from wtforms import Form, StringField, PasswordField, validators, BooleanField
from wtforms.validators import InputRequired



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
    def tocheck_paycondition(self, connection):
       list_customer_paycondition = []
       list = []
       connection.execute("SELECT * FROM job WHERE paid = 0;")
       customerlist = connection.fetchall()
       for i in range(len(customerlist)):
               list_customer_paycondition.append(str(customerlist[i][1]))
               list_customer_paycondition.append(customerlist[i][2])
               list_customer_paycondition.append(customerlist[i][3])
               list_customer_paycondition.append(customerlist[i][4])
               list_customer_paycondition.append(customerlist[i][5])
               list.append(list_customer_paycondition)
               list_customer_paycondition = []
               print(list)
       return list


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
    def toview_paymenthistory(customer_id, connection):
       list_customer_paycondition = []
       list = []
       connection.execute("SELECT * FROM job WHERE paid = 1;")
       customerlist = connection.fetchall()
       for i in range(len(customerlist)):
               list_customer_paycondition.append(str(customerlist[i][1]))
               list_customer_paycondition.append(customerlist[i][2])
               list_customer_paycondition.append(customerlist[i][3])
               list_customer_paycondition.append(customerlist[i][4])
               list_customer_paycondition.append(customerlist[i][5])
               list.append(list_customer_paycondition)
               list_customer_paycondition = []
               print(list)
       return list

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


    def get_next_partid(self, connection):
        connection.execute('select max(part_id) from part;')
        id = connection.fetchall()
        id = id[0][0] + 1
        return id

    def get_next_jobid(self, connection):
        connection.execute('select max(job_id) from job;')
        id = connection.fetchall()
        id = id[0][0] + 1
        return id

    def get_next_customer(self, connection):
        connection.execute('select max(customer) from job;')
        id = connection.fetchall()
        id = id[0][0] + 1
        return id
