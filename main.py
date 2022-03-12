import shutil
import os


# Please add the character "/" to the end of the path like that:
# Don't use "\" if you are in Windows, use "/".
# C:/Users/NewUser/Downloads(/) <---- This simbol to the end
original_path = '' # <-- Write here.

# Write folder's name
# Type all the names of the folders that will store the files.
# You can add or delete the ones you want, we have some by default.
folders_name = ['jpg','mp3', 'mp4','exe', 'pdf','rar','docs', 'txt']

# Global variables
# Add the main's path (Where are every files)
all_files = os.listdir(path='') #<-- Write here (This path please without the simbol to the end) Ex: C:/Users/NewUser/Downloads
files_name = [] # <- Don't change nothing.

# Variables for extensions to move to a folder.
# Here you add one variable per folder, and add between the square brackets the file extensions that this folder will be able to store.
jpg_folder_extensions = ['.jpg','.png','.svg','.ico','.jpeg']
mp3_folder_extensions = ['.mp3','.mpeg']
mp4_folder_extensions = ['.mp4','.mkv']
exe_folder_extensions = ['.exe','.msi', '.jar','.iso','.vbox-extpack', '.ova']
pdf_folder_extensions = ['.pdf']
rar_folder_extensions = ['.rar','.zip']
txt_folder_extensions = ['.txt', '.log']
docs_folder_extensions = ['.doc','.docx']



# Please add the names of the variables of up.
extensions_folders = [jpg_folder_extensions, mp3_folder_extensions, mp4_folder_extensions, exe_folder_extensions, pdf_folder_extensions, rar_folder_extensions, txt_folder_extensions, docs_folder_extensions]

# Please write as in the example:
# 'folder's name':'variable's name of the extensions'
meaning_of_extensions = {'jpg':'jpg_folder_extensions', 'mp3':'mp3_folder_extensions', 'mp4': 'mp4_folder_extensions', 'exe':'exe_folder_extensions','pdf':'pdf_folder_extensions','rar':'rar_folder_extensions','txt':'txt_folder_extensions','docs':'docs_folder_extensions'}

# Functions zone
def generate_folders_path(folders_name, original_path):
    folders_path = []
    for _ in range(len(folders_name)):
        new_rute = original_path+folders_name[_]
        folders_path.append(new_rute)
    return folders_path


def read_files_name():
    for i in range(len(all_files)):
        condition = False
        for _ in range(len(folders_name)):
            if all_files[i] == folders_name[_]:
                condition = True
                break
        if condition == True:
            continue
        files_name.append(all_files[i])


def generate_files_path(files_name):
    files_path = []
    for i in range(len(files_name)):
        new_files_path = original_path+files_name[i]
        files_path.append(new_files_path)
    return files_path


def select_destination_path(files_name, original_path,extensions_folders,files_path_to_extentions):
    dict_file_to_folder = {}
    for file in range(len(files_name)):
        variables = dict(globals())
        for _ in range(len(extensions_folders)):
            for x in range(len(extensions_folders[_])):
                if files_path_to_extentions[files_name[file]] == extensions_folders[_][x]:
                    for name in variables:
                        if variables[name] is extensions_folders[_]:
                            folders_name = name
                            break
                    dict_file_to_folder[files_name[file]] = folders_name
    

    for key in dict_file_to_folder:
        for _ in meaning_of_extensions:
            if dict_file_to_folder[key] == meaning_of_extensions[_]:
                dict_file_to_folder[key] = list(meaning_of_extensions.keys())[list(meaning_of_extensions.values()).index(meaning_of_extensions[_])]

    for key in dict_file_to_folder:
        new_destination_path = str(original_path + dict_file_to_folder[key]+"/"+ key)
        dict_file_to_folder[key] = new_destination_path
    
    return dict_file_to_folder


def get_file_extension(files_name):
    files_extensions = []

    for i in range(len(files_name)):
        extension_detector = []
        for caracter in files_name[i]:
            if caracter == ".":
                extension_detector.clear()
                continue
            else:
                extension_detector.append(caracter)
        extension_detector.insert(0,".") 
        extension_file = "".join(extension_detector)
        files_extensions.append(extension_file)
    return files_extensions


def move_files_to_folder(destinations_path,files_path,files_name):
    counter = 0
    for file in files_path:
        try:
            original = r'{file}'.format(file=file)
            target = r'{path_destination}'.format(path_destination=destinations_path[files_name[counter]])
            counter += 1
            shutil.move(original, target)
        except:
            counter += 1
            continue
        
    
# Main FUNCTION
def run():
    read_files_name()
    # Generate folders path
    folders_path = generate_folders_path(folders_name, original_path)

    files_path = generate_files_path(files_name)
    files_extensions = get_file_extension(files_name)
    files_path_to_extentions = {}
    for _ in range(len(files_name)):
        files_path_to_extentions[str(files_name[_])] = str(files_extensions[_])

    destinations_path = select_destination_path(files_name, original_path,extensions_folders,files_path_to_extentions)

    move_files_to_folder(destinations_path,files_path, files_name)
    print("[+] Successful operation")

if __name__ == '__main__':
    try:
        run()
    except:
        "[-] An error interrupted the operation."
