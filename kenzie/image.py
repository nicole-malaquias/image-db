import os
import zipfile
import dotenv 
from dotenv import load_dotenv


FILES_DIRECTORY = os.getenv('FILES_DIRECTORY')

ALLOWED_EXTENSIONS = { 'png', 'jpg', 'gif'}


def create_image_foud() :
    try:
        os.mkdir("image")   
    except:
        return ''


def allowed_file(filename):
    
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
           

def how_many_pic(path,name):

    arr = list(path)[0][2]
    return name in arr
        

def load_all_archive(path):
    
    temp = list(os.walk(path))
    arr = temp[0][-1]
    response = [ i for i in arr if i[-2:] != '.py']
    
    return response

def load_to_type(path,tipo):
    
    temp = list(os.walk(path))
    arr= temp[0][-1]
    arr_new = [i for i in arr if i[-3:] == tipo]
    return arr_new



def find_arch(name):
   
    path = "/home/nicole/Área de Trabalho/Kenzie/Q3/sprint-2/entrega6/image"
    temp = list(os.walk(path))
    arr = temp[0][-1]
    file = [i for i in arr if name in i ]
    return file 
    


def compact_zip(kind, nivel):
    
    path = FILES_DIRECTORY+'/image/'
    cont = 0 
    arquivo_zip = zipfile.ZipFile(path+'/archive.zip', 'w')
    
    for folder, _ ,files in os.walk( path):

        for file in files:
            if file.endswith(kind):
                arquivo_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file),path), compress_type = zipfile.ZIP_DEFLATED,compresslevel=nivel)
                cont = cont + 1 
    arquivo_zip.close()
    if cont == 0:
        return 0 
    return arquivo_zip
    
     
     
     