import os
import shutil as sh
# 이건 경로에서 마지막에 위치한 file 이름을 얻기위한 library
import ntpath

##############################!@ 수정할 내용들##############################################
target_dir = os.getcwd()
# target_dir = "D:\\00_AI_application\\P#2_DT1_AOI_AI_vision\AOI_result"
created_folder_name = "NTF_file_collected"
DESTIN_DIR =os.path.join(target_dir, created_folder_name)
##########################################################################################

# 이 함수로 원하는 경로에 folder를 생성한다.
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)

# 이 함수로 list를 만드는데, list에 들어가는 값들은 full_path명을 가진다.
# 조건은 1.folder에 들어가있어야 하고, 2. 확장자가 .pyc가 아니고, 3.folder명이 "NTF_file_collected"가 아닌 것들이다.
file_list = []
def bong_get_list(root_dir):
    # 아래로 list에 현재 folder에 존재하는 모든 folder path를 넣는다.
    list = []
    files = os.listdir(root_dir)
    for file in files:
        path = os.path.join(root_dir, file)
        list.append("" + path)
    # file_list에는 가불량 이미지가 존재하는 folder에 들어가서 해당 folder의 모든 file이름을 담아 조건에 맞는 file path+name을 list에 담아 return한다.
    for i in list:
        # i가 folder이면 계속하고, file이면 다음 작업 하지 마라 (현재 폴더에 file이 존재할 경우에는 아래 작업할 필요가 없다)
        # 확장자가 .pyc라는 파일이 계속 detect되는데 이거 제거 / "NG_collected" folder도 제거
        if os.path.isdir(i) and i != r'.pyc' and ntpath.basename(i) != created_folder_name:

            files_name = os.listdir(i)
            #  folder path에 접근해서 해당 folder에 file이 하나 이상 존재하면
            #  해당 folder의 file들을 full path로 file_list에 저장한다.
            if len(files_name) > 1:
                for one_file_name in files_name:
                    # "CURRENTA.JPG" file은 skip하자!
                    if one_file_name == "CURRENTA.JPG":
                        pass
                    else:
                        file_path = os.path.join(i, one_file_name)
                        file_list.append(file_path)
    # return file_list
createFolder(DESTIN_DIR)
bong_get_list(target_dir)

for bong in file_list:
    bong_name = ntpath.basename(bong)
    sh.move(bong, DESTIN_DIR + '/' + bong_name)






