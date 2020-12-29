# kaggle-ranzcr

#### Kaggle RANZCR CLiP - notebooks and dataset for collaboration.

## Run Project
```
docker-compose up
```
<img src="https://github.com/LilySu/kaggle-ranzcr/blob/master/images/setup/docker-compose_up.PNG?raw=true"> 

#### After pasting in the last url ie. http://127.0.0.1:8888/?token=a189b4479bf20dc53581f588cc36f392c0f2a6870509890b into your browser.

### Size

<img src="https://github.com/LilySu/kaggle-ranzcr/blob/master/images/setup/docker_image_size_and_name.PNG?raw=true"> 

#### Docker Image Size: 2.25 MB - amount of data (on disk) that is used for the writable layer of the container.

#### Docker Virtual Repository Size: 6.93 GB - shows the combined size of the readonly layer (the image), and the writable layer of the container shared between containers.

#### [For more info on storage usage](https://stackoverflow.com/questions/37966973/what-is-the-difference-between-the-size-and-the-virtual-size-of-the-docker-image)

## What You Get

#### - 4 Starter notebooks from public kaggle notebooks
#### - It is recommended to start with the catheter-position-exploratory-data-analysis.ipynb notebook
#### - Cuda is not supported at this time
#### - Pytorch is not installed yet. 
#### - To install Pytorch, open a terminal inside the running Jupyter instance and run:
 ```conda install pytorch torchvision torchaudio cpuonly -c pytorch -y```

#### Inside the Jupyter Notebook:
##### notebooks folder
#### After pasting in the last url ie. http://127.0.0.1:8888/?token=a189b4479bf20dc53581f588cc36f392c0f2a6870509890b this is what you get:

<img src="https://github.com/LilySu/kaggle-ranzcr/blob/master/images/setup/after_pasting_in_the_last_url.PNG?raw=true">

##### data_sample folder
 - contains full .csv's from the Ranzcr CLiP competition
 - contains a small sampling of .jpg data in the train and test folders
 - does not include .tfrec tensorflow files due to github file size limit


## Copy Your Kaggle Data from your Computer into the Docker Container

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
