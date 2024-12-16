from flask import Flask, render_template, request, redirect, url_for
import datetime

app = Flask(__name__)

# Mock database
tasks = []


@app.route('/')
def home():
    return render_template('index.html', tasks=tasks)


@app.route('/add_task', methods=['POST'])
def add_task():
    task_name = request.form['task_name']
    start_time = request.form['start_time']
    end_time = request.form['end_time']

    # Calculate time spent
    fmt = '%H:%M'
    try:
        time_spent = datetime.datetime.strptime(end_time, fmt) - datetime.datetime.strptime(start_time, fmt)
        tasks.append({
            'name': task_name,
            'start_time': start_time,
            'end_time': end_time,
            'time_spent': time_spent,
        })
    except ValueError:
        time_spent = "Invalid time format"

    return redirect(url_for('home'))


@app.route('/clear_tasks', methods=['POST'])
def clear_tasks():
    tasks.clear()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
