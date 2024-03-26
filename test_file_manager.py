import file_manager as fm
import os
import shutil


def test_make_folder():
    test_folder_name = 'test_make'

    if os.path.exists(test_folder_name):
        fm.remove_file_or_folder(test_folder_name)

    message = fm.make_folder(test_folder_name)

    assert message == f"Папка '{test_folder_name}' успешно создана."

    fm.remove_file_or_folder(test_folder_name)


def test_remove_file_or_folder():
    test_folder_name = 'test_remove'

    if not os.path.exists(test_folder_name):
        fm.make_folder(test_folder_name)

    message = fm.remove_file_or_folder(test_folder_name)

    assert message == f"Папка '{test_folder_name}' была удалена."

    message = fm.remove_file_or_folder(test_folder_name)

    assert message == "Файл или папка не найдены."


def test_copy_file_or_folder():

    test_folder_source = 'test_copy_src'
    test_folder_destination = 'test_copy_destination'

    if os.path.exists(test_folder_source):
        fm.remove_file_or_folder(test_folder_source)

    message = fm.copy_file_or_folder(test_folder_source, test_folder_destination)

    assert message == f'Не найдено файла или папки с названием {test_folder_source}'

    fm.make_folder(test_folder_source)

    if not os.path.exists(test_folder_destination):
        fm.make_folder(test_folder_destination)

    message = fm.copy_file_or_folder(test_folder_source, test_folder_destination)

    assert message == f"Папка '{test_folder_source}' скопирована в '{test_folder_destination}'"

    fm.remove_file_or_folder(test_folder_source)
    fm.remove_file_or_folder(test_folder_destination)


def test_list_dir():

    test_new_dir = 'test_list_dir_new'
    test_dir = 'test_list_dir'

    if os.path.exists(test_new_dir):
        fm.remove_file_or_folder(test_new_dir)

    fm.make_folder(test_new_dir)
    fm.change_work_directory(test_new_dir)

    fm.make_folder(test_dir)

    obj_list = fm.list_dir()

    assert obj_list == [test_dir]

    fm.change_work_directory('..')
    fm.remove_file_or_folder(test_new_dir)


def test_change_work_directory():
    test_change_dir = 'test_change_dir'

    if os.path.exists(test_change_dir):
        fm.remove_file_or_folder(test_change_dir)

    fm.make_folder(test_change_dir)

    source_current_dir = os.getcwd()
    message = fm.change_work_directory(test_change_dir)
    destination_current_dir = os.path.join( source_current_dir, test_change_dir)

    assert message == f"Текущая рабочая директория изменена на: {destination_current_dir}"

    fm.change_work_directory('..')
    fm.remove_file_or_folder(test_change_dir)


def test_save_current_dir():

    test_new_dir = 'test_save_current_dir_new'
    test_dir = 'test_save_current_dir'
    test_file = 'test_save_current_file.txt'

    if os.path.exists(test_new_dir):
        shutil.rmtree(test_new_dir)

    os.makedirs(test_new_dir, exist_ok=True)
    os.chdir(test_new_dir)

    os.makedirs(test_dir, exist_ok=True)

    save_current_dir_message = fm.save_current_dir(test_file)

    files_list = []
    folders_list = []
    contents = os.listdir()
    for item in contents:
        if os.path.isdir(item):
            folders_list.append(item)
        if os.path.isfile(item):
            files_list.append(item)

    with open(test_file, 'r') as f:
        files_line = f.readline().rstrip()
        folders_line = f.readline()

    assert save_current_dir_message == f"В файл {test_file} сохранено {len(files_list)} файлов и {len(folders_list)} папок"
    assert files_line == 'files: '+', '.join(files_list)
    assert folders_line == 'dirs: ' + ', '.join(folders_list)

    os.chdir('..')
    shutil.rmtree(test_new_dir)
