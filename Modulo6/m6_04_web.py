from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/python_run')
def index():
    return render_template('launcher.html')

@app.route('/run_action', methods=['POST'])
def run_script():
    # Recupera i dati dal form
    anno = request.form['anno']
    mese = request.form['mese']

    cmd = f"/home/pentaho/etl/valsabbina/script/job_load_all.sh {anno} {mese}"
    #subprocess.Popen(comando, shell=True)

    # Esegui il comando shell
    try:
        # result = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # output = result.stdout.decode('utf-8')
        # error = result.stderr.decode('utf-8')
        # return f'<h1>Job Output</h1><pre>{output}</pre><h1>Job Error</h1><pre>{error}</pre>'
        return f'<h1>Anno</h1><pre>{anno}</pre><h1>Mese</h1><pre>{mese}</pre>'
    except subprocess.CalledProcessError as e:
        return f'<h1>Error</h1><pre>{e}</pre>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)