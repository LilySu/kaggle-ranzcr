# kaggle-ranzcr

#### Kaggle RANZCR CLiP - notebooks and dataset for collaboration.

## Run Project
```
docker-compose up
```
<img src="https://github.com/LilySu/kaggle-ranzcr/blob/master/images/setup/docker-compose_up.PNG?raw=true"> 

##### After pasting in the last url ie. http://127.0.0.1:8888/?token=a189b4479bf20dc53581f588cc36f392c0f2a6870509890b

#### Inside the Jupyter Notebook
<img src="https://github.com/LilySu/kaggle-ranzcr/blob/master/images/setup/after_pasting_in_the_last_url.PNG?raw=true">

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
