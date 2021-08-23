from app import app
import os 

test_client = app.test_client()


def test_list_files_doesnt_accepts_post():
    
    assert test_client.post('/files').status_code == 405 


def test_list_files_accepts_get():
    
    assert 'GET' in test_client.options('/files').headers['allow']
    

def test_list_files_types_accepts_get():
    
    assert 'GET' in test_client.options('/files/<type>').headers['allow']
    

def test_list_files_by_name_exists():
    path_all = './image'
    extension = 'png'
    arr_extension = []
    temp = list(os.walk(path_all))
    for i in temp :
        end = str(i).split('.')[-1]
        arr_extension.append(end[:-3])
    assert extension in arr_extension
    

def test_if_archive_existe_in_foud():
    path_all = './image/'
    file_name = 'file'
    arr_name_files = []
    temp = list(os.walk(path_all))[0][-1]
    for i in temp :
        name = i.split('.')[0]
        arr_name_files.append(name)
    assert file_name in arr_name_files
    

def test_if_doesnt_accepts_post():   
    
    assert test_client.post('/download/file').status_code == 405
    
    


    
    
# Rota de listagem '/files';  ok 
# Rota de listagem por tipo '/files/<type>';   ok 
# Rota de dowload por nome de arquivo '/download/<file_name>'; ok 
# Rota de dowload ZIP '/download-zip';
# Rota de upload '/upload';
