from flask import Flask , jsonify, request
from dotenv import load_dotenv
import os
from kenzie import allowed_file, how_many_pic ,load_environment_variable,load_all_archive,load_to_type
load_dotenv()
load_environment_variable()


app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024
app.config['FILES_DIRECTORY'] = "/home/nicole/Área de Trabalho/Kenzie/Q3/sprint-2/entrega6/image"


@app.route('/upload',methods=["POST"])
def post_uplode():
    arquivos = request.files["file"]
    is_allowed = allowed_file(str(arquivos.filename))
    caminho = os.walk("/home/nicole/Área de Trabalho/Kenzie/Q3/sprint-2/entrega6/image")
    has_pic = how_many_pic(*caminho,arquivos.filename)
    if has_pic:
        return {"msg":"arquivo já existe"},409
    if is_allowed:
        arquivos.save(os.path.join("/home/nicole/Área de Trabalho/Kenzie/Q3/sprint-2/entrega6/image", arquivos.filename))
        return jsonify(arquivos.filename),201
    else :
        return {"msg": "file type is not allowed "},415


@app.route("/files", defaults={'tipo': None})
@app.route("/files/<tipo>")
def get_files(tipo):
    arch_in_path = load_all_archive("/home/nicole/Área de Trabalho/Kenzie/Q3/sprint-2/entrega6/image/")
    if tipo :
        arch_type = load_to_type("/home/nicole/Área de Trabalho/Kenzie/Q3/sprint-2/entrega6/image/",tipo)
        return jsonify(arch_type) 
    return jsonify(arch_in_path)


@app.route("/download/<file_name>")
def get_download_file(file_name):
    return send_from_directory(directory="../image", path="dog.png", as_attachment=True)
    
    """
    responsavel por fazer o download do arquivo name
    que é solicitado em fileName
    """

# @app.route("download-zip")
# def get_download_zip():
#     ...

# @app.route("/")
# def diretorio():
#     os.system("mkdir diretorio-novinho")
#     return 'criado'
