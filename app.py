from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL


app = Flask(__name__)

# Configuração do MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'fatec'
app.config['MYSQL_DB'] = 'MBViajens'
mysql = MySQL(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/serviços')
def serviços():
    return render_template('serviços.html')

@app.route('/contatos')
def contatos():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM contato")
    contato = cur.fetchall()
    cur.close()
    return render_template('contatos.html',contato=contato)

# Adicionar contato
@app.route('/add', methods=['POST'])
def add_contato():
    if request.method == 'POST':
        ir_de= request.form['ir_de']
        ir_para = request.form['ir_para']
        data_ida = request.form['data_ida']
        data_volta = request.form['data_volta']
        descrição = request.form['descrição']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contato (ir_de, ir_para, data_ida, data_volta, descrição) VALUES (%s, %s, %s, %s, %s)", (ir_de, ir_para, data_ida, data_volta, descrição))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('contatos'))

if __name__ == '__main__':
    app.run(debug=True)
