# kaggle-ranzcr

#### [Kaggle RANZCR CLiP](https://www.kaggle.com/c/ranzcr-clip-catheter-line-classification/overview) notebooks and sample dataset for collaborative purposes.
#### [About the Dataset](https://www.kaggle.com/c/ranzcr-clip-catheter-line-classification/data)
####  [How the Prediction is Evaluated](https://www.kaggle.com/c/ranzcr-clip-catheter-line-classification/overview/evaluation)

## Run Project
```
docker-compose up
```
<img src="https://github.com/LilySu/kaggle-ranzcr/blob/master/images/setup/docker-compose_up.PNG?raw=true"> 

#### Paste in the last url ie. http://127.0.0.1:8888/?token=a189b4479bf20dc53581f588cc36f392c0f2a6870509890b into your browser to run the jupyter notebook instance.
#### This is what the root directory of the jupyter notebook looks like.

<img src="https://github.com/LilySu/kaggle-ranzcr/blob/master/images/setup/after_pasting_in_the_last_url_root_directory.PNG?raw=true"> 

### Size

<img src="https://github.com/LilySu/kaggle-ranzcr/blob/master/images/setup/docker_image_size_and_name.PNG?raw=true"> 

#### Docker Image Size: 2.25 MB - amount of data (on disk) that is used for the writable layer of the container.

#### Docker Virtual Repository Size: 6.93 GB - shows the combined size of the readonly layer (the image), and the writable layer of the container shared between containers.
#### Virtual size is disk space that takes up space once - during the build of the container 

#### [For more info on storage usage](https://stackoverflow.com/questions/37966973/what-is-the-difference-between-the-size-and-the-virtual-size-of-the-docker-image)

## What You Get

#### - 4 Starter notebooks from public kaggle notebooks
#### - It is recommended to start with the catheter-position-exploratory-data-analysis.ipynb notebook
#### - Cuda is not supported at this time
#### - Pytorch is not installed yet. 
#### - To install Pytorch, open a terminal inside the running Jupyter instance and run:
 ```conda install pytorch torchvision torchaudio cpuonly -c pytorch -y```

### Inside the Jupyter Notebook:
#### notebooks folder:

<img src="https://github.com/LilySu/kaggle-ranzcr/blob/master/images/setup/after_pasting_in_the_last_url.PNG?raw=true">

#### data_sample folder:
 - contains full .csv's from the Ranzcr CLiP competition
 - contains a small sampling of .jpg data in the train and test folders
 - does not include .tfrec tensorflow files due to github file size limit


## Copy Your Kaggle Data from your Computer into the Docker Container
##### Pre-step:
 - To first download the Kaggle Competition Full dataset form the CLI
 - 1 Kaggle.com > Account > Home > Create New API Token
 - 2 Save kaggle.json inside of a .kaggle directory in your home directory
 - 3 Run `kaggle competitions download -c ranzcr-clip-catheter-line-classification`

#### When you have the full Kaggle Dataset in a directory:
##### The example assumes the dataset is unzipped under a 'data' directory within the  project directory
- Step 1. Look up IMAGE name or CONTAINER ID
```
docker ps -a
```
The above command lists the containers available 
- Step 2. Copy Files
```
docker cp <RELATIVE SRC FOLDER> <IMAGE OR CONTAINER_ID:DEST FOLDER>
```
- Navigate to directory to copy files
- Get the relative path
- For example:
```
docker cp data kaggle-ranzcr_kaggle-second:data
```

#### What the Data Folder Looks like
<img src="https://github.com/LilySu/kaggle-ranzcr/blob/master/images/setup/data_folder_with_ranzcr_clip_dataset.PNG?raw=true">  



## Check
#### Check Container
```
docker ps -a
```

## Cleanup
#### Stop One Container
```
docker stop <CONTAINER_ID>
```

#### Remove All Containers
```
docker rm <CONTAINER_ID>
```

#### Remove Docker Images
```
docker rmi <CONTAINER_ID>
```

## Cleanup for All Containers

#### Stop All Containers
```
docker stop $(docker ps -aq)
```

#### Remove All Containers
```
docker rm $(docker ps -aq)
```

#### Remove Docker Images
```
docker rmi $(docker images -q)
```
