from flask import Flask, request, json,Response
import os
import logging
handler = logging.FileHandler('/var/log/app.log') # errors logged to this file
handler.setLevel(logging.ERROR) 
app = Flask(__name__)
cwd = os.getcwd()
app.logger.addHandler(handler)  # attach the handler to the app's logger


@app.route("/")
def hello():
    return "Service health check OK!\n"

@app.route('/pemtoppk',methods=["POST"])
def pemtoppk():
    if request.method == 'POST':
        try:
            output_filename = request.form.get('output_filename')
            pem_key = request.form.get('pem_key')
            #print ("print output filename ")
            #print (output_filename)
            #print ("print input pem key ")
            #print (pem_key)
            pemFileName = output_filename + ".pem"
            pemFile = open(pemFileName, "w")
            pemFile.write(pem_key)
            pemFile.close()
            ppkFileName = output_filename + ".ppk"
            os.system("puttygen " + pemFileName  + " -O private -o "+ ppkFileName)
            ppkFile = open(ppkFileName, "r")
            ppkKey = ppkFile.read()
            print (ppkKey)
            resp = Response(ppkKey,status=200,mimetype='text/html')
            os.system("rm -rf "+ pemFileName)
            os.system("rm -rf "+ ppkFileName)
            return resp
        except Exception as ex:
            app.logger.error(ex)
            print (ex)
            return Response(error = ex,status=400,mimetype='text/html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
