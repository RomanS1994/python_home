import shutil 

archive = shutil.make_archive("backup", 'zip', './Lesson_5/')
print(archive)

shutil.unpack_archive(archive, 'New_folder')
