from flask import Flask , jsonify, request, send_from_directory
import os
import dotenv 
from dotenv import load_dotenv
from kenzie import compact_zip,allowed_file, how_many_pic ,load_all_archive,load_to_type,find_arch


app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024
FILES_DIRECTORY = os.getenv('FILES_DIRECTORY')



@app.route('/upload',methods=["POST"])
def post_uplode():
    
    arquivos = request.files["file"]
    is_allowed = allowed_file(str(arquivos.filename))
    caminho = os.walk(FILES_DIRECTORY+"/image/") 
    has_pic = how_many_pic(*caminho,arquivos.filename)
    
    if has_pic:
        return {"msg":"arquivo já existe"},409
    if is_allowed:
        arquivos.save(os.path.join(FILES_DIRECTORY+"/image/", arquivos.filename))
        return jsonify(arquivos.filename),201
    else :
        return {"msg": "file type is not allowed "},415


@app.route("/files", defaults={'tipo': None})
@app.route("/files/<tipo>")
def get_files(tipo):
    arch_in_path = load_all_archive(FILES_DIRECTORY+"/image")
    if tipo :
        arch_type = load_to_type(FILES_DIRECTORY+"/image/",tipo)
        if len(arch_type) > 0:
         return jsonify(arch_type) 
        else :
            return {'msg': 'não há arquivos desse tipo'}
    return jsonify(arch_in_path)


@app.route("/download/<file>")
def get_download_file(file):  
    try :
        arch = find_arch(file)[0]
        return send_from_directory(directory="../image", path=arch, as_attachment=True)
    except IndexError:
        return {"msg": "Arquivo não existe"},404
        
    
@app.route("/download-zip")
def get_download_zip():
    type = str(request.args.get('file_type'))
    level = int(request.args.get('compression_rate'))
    zip = compact_zip(type,level)
    if zip == 0 :
        return {"msg":"Nao tem arquivos desse tipo"},404
    return send_from_directory(directory="../image", path='archive.zip', as_attachment=True)
    
