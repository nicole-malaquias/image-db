from flask import Flask , jsonify, request, send_from_directory
import os
import dotenv 
from dotenv import load_dotenv
from kenzie import image

image.create_image_foud()
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024
FILES_DIRECTORY = os.getenv('FILES_DIRECTORY')



@app.route('/upload',methods=["POST"])
def post_uploade():
    
    archive = request.files["file"]
    is_allowed = image.allowed_file(str(archive.filename))
    path = os.walk(FILES_DIRECTORY) 
    has_pic = image.how_many_pic(path,archive.filename)   
    
    if has_pic:
        return {"msg":"this archive exists "},409
    if is_allowed:
        archive.save(os.path.join(FILES_DIRECTORY, archive.filename))
        return jsonify(archive.filename),201
    return {"msg": "file type is not allowed "},415


@app.route("/files", defaults={'tipo': None})
@app.route("/files/<tipo>")
def get_files(tipo):
    arch_in_path = image.load_all_archive(FILES_DIRECTORY)
    if tipo :
        arch_type = image.load_to_type(FILES_DIRECTORY,tipo)
        if len(arch_type) > 0:
         return jsonify(arch_type) 
        else :
            return {'msg': "here is not have this archive type"}
    return jsonify(arch_in_path)


@app.route("/download/<file>")
def get_download_file(file):  
    try :
        arch = image.find_arch(file)[0]
        return send_from_directory(directory="../image", path=arch, as_attachment=True)
    except IndexError:
        return {"msg": "this archive exists"},404
        
    
@app.route("/download-zip")
def get_download_zip():
    try:
        type = str(request.args.get('file_type'))
        level = int(request.args.get('compression_rate'))
        zip = image.compact_zip(type,level)
        if zip == 0 :
            return {"msg":""},404
        return send_from_directory(directory="../image", path='archive.zip', as_attachment=True)
    except :
        return '',404
