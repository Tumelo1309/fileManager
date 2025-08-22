##sript should compare content from different directories
##file intersecting directories and share the difference in content
import os
import shutil

##gets the path
##changes it to a set
def listing_file(path):

    files = set(os.listdir(path))

    return files

def diff_files(set_one,set_two):

    temp_storage = list(set_one - set_two)
    file_storage = []

    for file in temp_storage:
        if not os.path.isdir(file):
            file_storage.append(file)

    return file_storage

def diff_dir(set_one,set_two):

    temp_storage = list(set_one - set_two)
    dir_storage = []

    for doc in temp_storage:
        if os.path.isdir(doc):
            dir_storage.append(doc)

    return dir_storage

##finds common files/directories
def common_content(set_one,set_two):

    return list(set_one & set_two)

#check if content is directory
def is_directory(path,content):

    full_path = os.path.join(path, content)

    return os.path.isdir(full_path)

#collects directories
def directories_list(path, common_names):
    doc_list = []

    for item in common_names:

        temp_path = os.path.join(path, item)

        if os.path.isdir(temp_path):
            doc_list.append(item)

    return doc_list

#collects files
def file_list(path, commonn_names):
    doc_list = []

    for item in commonn_names:

        temp_path = os.path.join(path, item)

        if not os.path.isdir(temp_path):
            doc_list.append(item)

    return doc_list


device_path = "/home/tumelo/Downloads"
usb_path = "/media/tumelo/TUM3L0"
device_set = listing_file(device_path)#path from device
usb_set = listing_file(usb_path)##usb path
common_list = common_content(device_set,usb_set)
common_files = file_list(device_path,common_list)
device_dir = diff_dir(device_set,usb_set)
usb_dir = diff_dir(usb_set,device_set)
device_file = diff_files(device_set,usb_set)
usb_file = diff_files(usb_set,device_set)

#moving from device to usb
if len(usb_file) > 0:
    for file in usb_file:
        temp_file = os.path.join(usb_path,file)
        shutil.move(temp_file,device_path)
        print(f"Moved file {file} to device")
else:
    print("Files match")


#moving from device to usb
if len(device_file) > 0:
    for file in device_file:
        temp_file = os.path.join(device_path,file)
        shutil.move(temp_file,usb_path)
        print(f"Moved file {file} to usb")
else:
    print("Files match")
# for file in common_files:
#     temp_device_file = os.path.join(device_path,file)
#     temp_usb_file = os.path.join(usb_path,file)
#
#     if os.path.getsize(temp_device_file) > os.path.getsize(temp_usb_file):
#         shutil.copy2(temp_device_file,temp_usb_file)
#         print(f"Successfully replace {file} from device to usb")
#         #print(f"Device {file} file is larger")
#
#     elif os.path.getsize(temp_device_file) == os.path.getsize(temp_usb_file):
#         print(f"{file} from device & device are equal")
#
#     else:
#         shutil.copy2(temp_usb_file,temp_device_file)
#         print(f"Successfully replace {file} from usb to device")