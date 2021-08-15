from flask import Flask , jsonify
from dotenv import load_dotenv
import os
load_dotenv()


app = Flask(__name__)


# @app.route('/upload')
# def post_uplode():
#     """
#     enviar o arquivo por formulario com o campo de nome file
#     e o valor é o arquivo que 
#     """
#     ...


# @app.route("/files", defaults={'tipo': None})
# @app.route("/files/<fipo>")
# def get_files(tipo):
#     """
#     listara todo os arquivos
#     listara todo os arquivos do tipo que vira no campo tipo 
#     """
#     if tipo :
#         return jsonify(tipo) 
#     return 'empty'


# @app.route("/download/<file_name>")
# def get_download_file(file_name):
#     """
#     responsavel por fazer o download do arquivo name
#     que é solicitado em fileName
#     """

# @app.route("download-zip")
# def get_download_zip():
#     ...

# @app.route("/")
# def diretorio():
#     os.system("mkdir diretorio-novinho")
#     return 'criado'
