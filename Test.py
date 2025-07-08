import os

def directories_list(path,commonn_names):

    doc_list = []

    for item in commonn_names:

        temp_path = os.path.join(path,item)

        if os.path.isdir(temp_path):
            doc_list.append(item)

    return doc_list