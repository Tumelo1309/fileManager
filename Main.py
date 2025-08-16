##sript should compare content from different directories
##file intersecting directories and share the difference in content

import os

##gets the path
##changes it to a set
def listing_file(path):

    files = set(os.listdir(path))

    return files

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
usb_path = "/media/tumelo/TUM3L0/"
device_set = listing_file(device_path)#path from device
usb_set = listing_file(usb_path)##usb path
common_list = common_content(device_set,usb_set)
common_files = file_list(device_path,common_list)
common_directories = directories_list(device_path,common_list)

