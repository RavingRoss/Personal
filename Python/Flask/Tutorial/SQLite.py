from flask import Flask, render_template, request
import sqlite3 as sq

conn = sq.connect('database.db')
print ("Opened database successfully")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/enternew')
def star():
    return render_template('stars.html')

@app.route('/data', methods = ['POST', 'GET'])
def data():
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            clas = request.form['class']
            const = request.form['const']
            coord = request.form['coord']

            with sq.connect("database.db") as conn:
                cur = conn.cursor()

                cur.execute("INSERT INTO stars (name, class, const, coord) VALUES (?,?,?,?)", (nm, clas, const, coord))
                
                conn.commit()
                msg = "Record successfully added"
        except: 
            conn.rollback()
            msg = "Error in insert option"

        finally:
            return render_template("results.html", msg = msg)
    conn.close()

@app.route('/list')
def list():
    conn = sq.connect("database.db")
    conn.row_factory = sq.Row

    cur = conn.cursor()
    cur.execute(" Select * from stars")

    rows = cur.fetchall()
    return render_template("list.html", rows = rows)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)