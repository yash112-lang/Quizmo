from django.http import HttpResponse
from django.shortcuts import render
import pymysql as mysql



def index(request):
    return render(request, "form.html")

# def register(request):
#     return render(request, "data.html", {"message":""})
def submit(request):
    fname = request.POST["fname"]
    lname = request.POST["lname"]
    organization_name = request.POST["oname"]
    email = request.POST["email"]
    password = request.POST["password"]
    cpassword = request.POST["cpassword"]
    profile = request.POST["profile"]
    name = fname + " " + lname
    conn = mysql.connect(host="localhost", port=3306, user="root", password="", db = "quizmo")
    cmd = conn.cursor()
    sql = f"INSERT INTO organization_register(fname, lname, email, organization_name, password, profile) VALUES('{fname}', '{lname}', '{email}', '{organization_name}', '{password}', '{profile}')"
    print(sql)
    cmd.execute(sql)
    conn.commit()
    conn.close()
    return render(request, 'sidebar.html')