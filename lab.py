from flask import Flask,jsonify, request
app = Flask("test")

tasks = [
    {
        'Name': 'Vitaliy',
        'SecondName': 'Cal',
        'Ages': 30,
        'phoneNum': '+7(934)-535-53-55',
        'profession': 'cybersportsman'
    },
    {
        'Name': 'Lebron',
        'SecondName': 'James',
        'Ages': 34,
        'phoneNum': '+243(925)-732-74-12',
        'profession': 'sportsman'
    },
    {
        'Name': 'Mike',
        'SecondName': 'Tyson',
        'Ages': 55,
        'phoneNum': '+231(732)-623-82-35',
        'profession': 'sportsman'
    },
    {
        'Name': 'Scarlett',
        'SecondName': 'Johansson',
        'Ages': 35,
        'phoneNum': '+7(920)-424-42-24',
        'profession': 'actress'
    },
    {
        'Name': 'Lana',
        'SecondName': 'Del Rey',
        'Ages': 37,
        'phoneNum': '+23(23)-232-32-32',
        'profession': 'singer'
    },
    {
        'Name': 'John',
        'SecondName': 'Doe',
        'Ages': 30,
        'phoneNum': '+XXX(XXX)-XXX-XX-XX',
        'profession': 'undefined'
    }

]

@app.route('/myPhoneBook/', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})
@app.route('/myPhoneBook/<int:index>', methods=['GET'])
def get_one_task(index):
    if index != 0:
        index -= 1
    if index<len(tasks):
        return jsonify({'tasks': tasks[index]})
    else:
        return jsonify({'error': "Wrong index"})
@app.route('/myPhoneBook/<int:index>', methods=['DELETE'])
def delete_tasks(index):
    if index != 0:
        index -= 1
    if index<len(tasks):
        del(tasks[index])
        return jsonify({'success': 'OK'})
    else:
        return jsonify({'error': "Wrong index"})


@app.route('/myPhoneBook/', methods=['PUT'])
def put():
    t=request.json['tasks']
    task = {}
    dop=''
    count = 0
    deside=['Name','SecondName','Ages','phoneNum','profession']
    for i in range(0,len(t)-1):
        task[deside[i]]=t[i+1]
        if(int(t[0])>0):
            tasks[int(t[0]) - 1] = task
        else:
            tasks[0]= task
    return jsonify({'success': 'OK'})

@app.route('/myPhoneBook/', methods=['POST'])
def post():
    print(request.json)
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif 'tasks' not in request.json.keys() :
        return jsonify({'error': 'Bad request'})
    t = request.json['tasks']
    '''    while string>0:
        if(string[0]==','):
            task[deside[count]] = dop
            dop = 0
            count+=1
            string = string[1:]
        dop+=string[0]
        string = string[1:]
    task[deside[count]] = dop
    dop = 0
    count += 1'''
    task = {}
    dop=''
    count = 0
    deside=['Name','SecondName','Ages','phoneNum','profession']
    for i in range(0,len(t)):
        task[deside[i]]=t[i]
    tasks.append(task)
    return jsonify({'success': 'OK'})



app.run(port=8088, host='127.0.0.1')
