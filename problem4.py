# # 4. Create a Flask app with a form that accepts user input and displays it.

# from flask import Flask,request,render_template

# app = Flask(__name__)

# @app.route('/')
# def html_code():
#     return render_template('problem4.html')

# @app.route('/show', methods=['POST', 'GET'])
# def user_details():
#     first_name = request.form.get('f_name')
#     print(type(first_name))
#     last_name = request.form.get('l_name')
#     result = first_name + last_name
#     return f"{first_name} and {last_name} : {result}"
    
# if __name__ == '__main__':
#     app.run(debug=True, port = 5002)


from flask import Flask, request,render_template

app = Flask(__name__)

@app.route('/')
def html_code():
    return render_template('problem4.html')

@app.route('/show', methods=['POST'])
def user_details():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    result = first_name + ' ' + last_name
    print(f"first_name:{first_name}, last_name:{last_name}")
    return result

if __name__ == '__main__':
    app.run(host= '0.0.0.0',port = 5000,debug=True)
