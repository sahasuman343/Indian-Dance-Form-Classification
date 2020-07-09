import os
import shutil
import pandas as pd
import random

df=pd.read_csv("train.csv")

dance=df["target"].unique()
#print(dance)
current_dir=os.getcwd()
print("Current Directory:",current_dir)
train_dir = os.path.join(current_dir,"train")
new_dir = os.path.join(current_dir,"train_data")
def make_dir(list,new_dir):
    os.mkdir(new_dir)
    try:
        for name in list:
            path=os.path.join(new_dir,name)
            os.mkdir(path)
        print("successful!!")
    except Exception as e:
        print("Error!",e)

def copy_files(df,list,image_path,new_dir):
    for name in list:
        temp=df[df["target"]==name]
        dest=os.path.join(new_dir,name)
        print("copying files to : ",dest)
        for image in temp["Image"]:
            src=os.path.join(image_path,image)
            n=shutil.copy(src,dest)
            print("Copied to :",n)
    print("Success :)")

def split_data(SOURCE, TRAINING, TESTING, SPLIT_SIZE):
    shuffle=random.sample(os.listdir(SOURCE),len(os.listdir(SOURCE)))
    train_data_length=int(len(os.listdir(SOURCE))*SPLIT_SIZE)
    test_data_length=int(len(os.listdir(SOURCE))-train_data_length)
    train_data=shuffle[0:train_data_length]
    test_data=shuffle[-test_data_length:]
    for x in train_data:
        train_temp=os.path.join(SOURCE,x)
        final_train=os.path.join(TRAINING,x)
        shutil.copyfile(train_temp,final_train)
    for x in test_data:
        test_temp=os.path.join(SOURCE,x)
        final_test=os.path.join(TESTING,x)
        shutil.copyfile(test_temp,final_test)
    print("Training and Validation folder created successfully :)")


            


if __name__ == "__main__":
    if os.path.exists(new_dir)==False:
        make_dir(dance,new_dir)
        image_dir = os.path.join(current_dir,"train")
        copy_files(df,dance,image_dir,new_dir)
    #create data directory
    train_path=os.path.join(current_dir,"data","train")
    valid_path=os.path.join(current_dir,"data","valid")
    os.makedirs(train_path)
    os.makedirs(valid_path)
    split_size=0.85
    for name in dance:
        src=os.path.join(new_dir,name)
        train_target=os.path.join(train_path,name)
        valid_target=os.path.join(valid_path,name)
        os.mkdir(train_target)
        os.mkdir(valid_target)
        print("Spliting Data...........  ", name)
        split_data(src,train_target,valid_target,split_size)

    

