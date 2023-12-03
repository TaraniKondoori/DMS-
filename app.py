
from flask import Flask, request, render_template
import csv

app = Flask(__name__, template_folder='static')

@app.route('/read', methods = ["GET","POST"])
def read():
    net_id = request.values.get("netid")
    net_id_index = 0
    print('Im here')
    with open('StudentDatabase.csv', 'r') as f:
        lines = f.readlines()
    for index, line in enumerate(lines):
        if index == 0:
            headers = line.strip().split(',')
            net_id_index = headers.index('Net ID')
        else:
            student_details = line.strip().split(',')
            print(net_id, net_id_index,student_details)
            if net_id == student_details[net_id_index]:
                return render_template('Read.html', headers=headers, data=[student_details])
    return render_template('Read.html', message = "Student Not Found")

@app.route('/delete', methods=["GET","POST"])
def delete():
    net_id = request.values.get("netid")
    net_id_index = 0
    found = False
    with open('StudentDatabase.csv', 'r') as f:
        lines = f.readlines()
    with open('StudentDatabase.csv', 'w') as f:
        for index, line in enumerate(lines):
            if index == 0:
                column_names= line.strip().split(',')
                net_id_index = column_names.index('Net ID')
                f.write(line)
            else:
                student_details = line.strip().split(',')
                if net_id != student_details[net_id_index]:
                    f.write(line)
                else:
                    found = True
    
    with open('StudentDatabase.csv', 'r') as f:
        lines = f.readlines()
    header = lines[0].strip().split(',')
    data = []
    for i in range(1, len(lines)):
        data.append(lines[i].strip().split(","))
    
    message = ""
    if not found:
        message = "Record doens't exist"
        
    return render_template('Delete.html', message=message, headers=header, data=data)

@app.route('/update', methods=["GET","POST"])
def update():
    netid = request.values.get("netid")
    fname = request.values.get("fname")
    lname = request.values.get("lname")
    mname = request.values.get("mname")
    major = request.values.get("major")
    net_id_index = 0
    found = False
    with open('StudentDatabase.csv', 'r') as f:
        lines = f.readlines()
    with open('StudentDatabase.csv', 'w') as f:
        for index, line in enumerate(lines):
            if index == 0:
                column_names= line.strip().split(',')
                net_id_index = column_names.index('Net ID')
                f.write(line)
            else:
                student_details = line.strip().split(',')
                if netid == student_details[net_id_index]:
                    f.write(str(fname) + ',' + str(mname) + ',' + str(lname) + ',' + str(netid) + ',' + major + '\n')
                    found = True
                else:
                    f.write(line)
        
        if found == False:
            f.write(str(fname) + ',' + str(mname) + ',' + str(lname) + ',' + str(netid) + ',' + major + '\n')
    
    with open('StudentDatabase.csv', 'r') as f:
        lines = f.readlines()
    header = lines[0].strip().split(',')
    data = []
    for i in range(1, len(lines)):
        data.append(lines[i].strip().split(","))
    return render_template('Update.html', headers=header, data=data)
    
@app.route('/update_html') 
def update_html():
    with open('StudentDatabase.csv', 'r') as f:
        lines = f.readlines()
    header = lines[0].strip().split(',')
    data = []
    for i in range(1, len(lines)):
        data.append(lines[i].strip().split(","))
    return render_template('Update.html', headers=header, data=data)

@app.route('/read_html') 
def read_html():
    return render_template('Read.html')

@app.route('/delete_html') 
def delete_html():
    with open('StudentDatabase.csv', 'r') as f:
        lines = f.readlines()
    header = lines[0].strip().split(',')
    data = []
    for i in range(1, len(lines)):
        data.append(lines[i].strip().split(","))
    return render_template('Delete.html', headers=header, data=data)

@app.route('/display_data') 
def display_data():
    with open('StudentDatabase.csv', 'r') as f:
        lines = f.readlines()
    header = lines[0].strip().split(',')
    data = []
    for i in range(1, len(lines)):
        data.append(lines[i].strip().split(","))
    print(header)
    return render_template('LoadData.html', headers=header, data=data)


@app.route('/') 
def run():
    return render_template('Home.html')

if __name__ == '__main__':
    app.run()