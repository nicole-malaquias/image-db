import os


ALLOWED_EXTENSIONS = { 'png', 'jpg', 'gif'}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
           

def how_many_pic(path,name):
    arr = list(path[2])
    return name in arr


def load_environment_variable():
    path = "/home/nicole/Área de Trabalho/Kenzie/Q3/sprint-2/entrega6"
    exist = os.path.isfile('.env')
    if exist == False :
        arquivo = open(".env", "a")
        arquivo.write(f'FILES_DIRECTORY="{path}"')
        arquivo.write(f'\nFLASK_ENV=development')
        arquivo.close()
    return ''
        

def load_all_archive(path) :
    temp = list(os.walk(path))
    arr = temp[0][-1]
    arr.pop()
    
    return arr

def load_to_type(path,tipo):
    temp = list(os.walk(path))
    arr= temp[0][-1]
    arr_new = [i for i in arr if i[-3:] == tipo]
    return arr_new








# def find_directory(filename):
    
#     if os.path.isdir(filename):
#         print("O diretório existe!")
#     else:
#         os.mkdir(PATH+"/requeriment")
        
        