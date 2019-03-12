import os
path = '/home/vikrame/Vikrame/Coding/SRM-hack/images/guns'
files = os.listdir(path)
i = 1

for file in files:
    os.rename(os.path.join(path, file), os.path.join(path, "{}.jpg".format(
			str(i).zfill(8))))
    i = i+1