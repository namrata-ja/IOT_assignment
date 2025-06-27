from flask import Flask, request
from utils.database import execute_query
from utils.database import execute_select_query

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def insert_info():
    # extract data from request form
    name = request.form.get('name')
    age = request.form.get('age')
    city = request.form.get('city')
    steps = request.form.get('steps')
    pulse = request.form.get('pulse')
    oxygen = request.form.get('oxygen')
    temp = request.form.get('temp')

    # create a query
    query = f"insert into healthData(name, age, city, steps, pulse, oxygen, temp) values('{name}', {age},'{city}', {steps} ,{pulse} ,{oxygen}, {temp})"


    # execute a query
    execute_query(query)

    # return response
    return f"person with uid = '{name}' is inserted successfully\n"

@app.route('/all', methods=['GET'])
def get_info():
    # create a select query
    query = "select * from healthData;"

    # execute the query
    health = execute_select_query(query=query)

    # return persons list into response
    return health

@app.route('/info', methods=['GET'])
def user_info():
    name = request.form.get('name')
    query = "select * from healthData where name = 'xyz';"

    health = execute_select_query(query=query)

    return health

@app.route('/update', methods=['PUT'])
def update_user():
    name = request.form.get('name')
    oxygen = request.form.get('oxygen')

    query = f"update persons SET oxygen = {oxygen} where name = '{name}';"

    execute_query(query)

    return f"oxygen of user with name = '{name}' is updated successfully"


@app.route('/steps', methods=['GET'])
def max_steps():
  
    query = "SELECT * FROM health ORDER BY steps DESC LIMIT 1;"
    max= execute_query(query)

    return max

if __name__ == '__main__':
    app.run(debug=True)