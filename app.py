from flask import Flask, request, json, Response
import os
app = Flask(__name__)


@app.route("/")
def hello():
    return "Service health check OK!\n"


@app.route('/pemtoppk', methods=["POST"])
def pemtoppk():
    if request.method == 'POST':
        try:
            pem_key = request.form.get('pem_key')
            print("pem_key: ", pem_key)
            pemFileName = "key.pem"
            pemFile = open(pemFileName, "w")
            pemFile.write(pem_key)
            pemFile.close()
            ppkKey = os.system("puttygen " + pemFileName + " -O private")
            print("ppkKey: ", ppkKey)
            resp = Response(ppkKey, status=200, mimetype='text/html')
            return resp
        except Exception as ex:
            print(ex)
            return Response(status=500, mimetype='text/html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
