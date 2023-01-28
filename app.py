from flask import Flask,render_template,request,redirect,session
app = Flask(__name__)

dbo=Database()


@app.route('/')
def hello_world():  # put application's code here
    return render_template('login.html')
@app.route('/register')
def register():
    return render_template('register.html')
@app.route('/perform_registration',methods=['post'])
def perform_registration():
    name=request.form.get('user_ka_name')
    email=request.form.get('user_ka_email')
    password=request.form.get('user_ka_password')

    response=dbo.insert(name,email,password)

    if response:
        return render_template('login.html',message="Registration successful.Kindly login to proceed")
    else:
       return render_template('register.html',message='Email already exists')

@app.route('/perform_login',methods=['post'])
def perform_login():
    email=request.form.get('user_ka_email')
    password=request.form.get('user_ka_password')
    response=dbo.search(email,password)

    if response:
        session['logged_in'] = 1
        return redirect('/profile')
    else:
        return render_template('login.html',message='incorrect email/password')

@app.route('/profile'):
def profile():
    if session['logged_in']==1:
       return render_template('profile.html')
    else:
        return redirect('/')

@app.route('/ner')
def ner():
    if session['logged_in'] == 1:
       return render_template('ner.html')
    else:
        return redirect('/')

@app.route('/perform_ner',methods=['post'])
def perform_ner():
    if session['logged_in']==1:
       text=request.form.get('ner_text')
       response=api.ner(text)
       print(response)
       result=''
       for i in response['entities']:
           result=result+i['name']+"==>"+i['category']+"\n"
          return render_template('ner.html',result=result)
    else:
        return redirect('/')
@app.route('/ser')
def ser():
    if session['logged_in'] == 1:
        return render_template('ser.html')
    else:
        return redirect('/')


@app.route('/perform_ser',methods=['post'])
def perform_ser():
    if session['logged_in'] == 1:
       text=request.form.get('ser_text')
       response=api.ser(text)
       print(response)
       result=''
       for i in response['sentiment']:
           result=result+i['negative'] + "==>" + i['positive'] + "==>" + i['neutral'] + "\n"
          return render_template('ser.html',result=result)
    else:
        return redirect('/')

@app.route('/abuse')
def abuse():
    if session['logged_in'] == 1:
          return render_template('abuse.html')
    else:
        return redirect('/')
@app.route('/perform_abuse' methods=['post'])
def perform_abuse():
    if session['logged_in'] == 1:
        request.form.get('abuse_text')
        response=api.abuse(text)
        print(response)
        result=''
        for i in response['abuse']:
            result=result+i['abusive'] + "==>" + i['hate_speech'] + "==>" i['neither'] + "\n"
            return render_template('abuse.html',result=result)
        else:
            return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
