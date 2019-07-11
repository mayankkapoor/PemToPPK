# PemToPPK

Description: This is a simple python program to convert .pem key file to .ppk file.

How to run ?

1. docker pull mayankkapoor/pemtoppk
2. docker run -d -p 5000:5000 mayankkapoor/pemtoppk

Open Postman client to test

API URL: http://localhost:5000/pemtoppk

REQ Type: POST
Body: In form-data, enter following key value data
```
{
"pem_key":"paste your RSA format .pem key in text format"
"output_filename": "Input some ppk file name"
}
```
It is very important to input the pem_key in RSA format only, otherwise
the service will throw an error.
PEM or base64 format key example:

-----BEGIN RSA FOO BAR KEY-----
MIIBgjAcBgoqhkiG9w0BDAEDMA4ECKZesfWLQOiDAgID6ASCAWBu7izm8N4V
2puRO/Mdt+Y8ceywxiC0cE57nrbmvaTSvBwTg9b/xyd8YC6QK7lrhC9Njgp/
...
-----END RSA FOO BAR KEY-----

Response:
Content of .ppk file in text format.
