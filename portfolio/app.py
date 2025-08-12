from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    
    personal_info = {
        'name': 'Manikanta Sreeram Undi',
        'title': 'Python Developer Intern',
        'bio': 'Welcome to my portfolio! I am passionate about web development and eager to learn Flask.',
        'skills': ['Python', 'Flask', 'HTML', 'CSS', 'JavaScript (basic)'],
        'email': 'your.email@example.com'
    }
    return render_template('index.html', info=personal_info)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        print(f"Received contact form submission from: {name} ({email})\nMessage: {message}")
        return redirect(url_for('home'))
    return render_template('contact.html')

@app.route('/about/<name>')
def about_person(name):
    return render_template('about.html', person_name=name)


if __name__ == '__main__':
    app.run(debug=True) 