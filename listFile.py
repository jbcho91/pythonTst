import os
import shutil


def list_files_in_directory(directory):
    # 지정된 디렉토리의 파일 리스트를 가져옴
    files = os.listdir(directory)

    # 파일 리스트 출력
    print("폴더 '{}' 내의 파일 리스트:".format(directory))
    for file in files:
        if os.path.isfile(os.path.join(directory, file)):
            print(file)
            if "aaa" in file:
                print("aaa "+file)
                shutil.move(os.path.join(directory, file), folder_path+"/aaa")


# 폴더 경로 지정
folder_path = ''

# 폴더 내 파일 리스트 출력
list_files_in_directory(folder_path)