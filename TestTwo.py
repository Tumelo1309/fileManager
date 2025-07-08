import os


def listing_file(path):

    files = set(os.listdir(path))

    return files

#check if content is directory
def is_directory(path,content):

    full_path = os.path.join(path, content)

    return os.path.isdir(full_path)

def similar_names(set_one,set_two):

    matching = []

    for item_one in set_one:
        for item_two in set_two:

            if item_one == item_two:
                print("Match found: " + item_one)
                matching.append(item_one)

    return matching

device_path = "/home/tumelo/Downloads"
usb_path = "/media/tumelo/TUM3L0/"

device_set = listing_file(device_path)
usb_set = listing_file(usb_path)
matching_content = similar_names(usb_set,device_set)


for item in matching_content:

    if is_directory(device_path,item):

