import os

def count_by_type(folder):
    counts = {}
    for filename in os.listdir(folder):
        old_path = os.path.join(folder,filename)
        if not os.path.isfile(old_path):
            continue
        ext =  os.path.splitext(filename)[1].lower()
        counts[ext] = counts.get(ext,0)+1
          
    return counts


data =  count_by_type("test_folder")
print(data)


    