##### .oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.


#### Copy Files From Your Local Computer into this Docker Container
- Step 1. Look up IMAGE name or CONTAINER ID
```
docker ps -a
```
The above command lists the containers available 
- Step 2. Copy Files
```
docker cp <SRC> <DEST>
```
- Navigate to directory to copy files
- Get the relative path
- For example:
```
docker cp data jupyter-tensorflow-notebook:data
```
- Explaination of above: in the local directory, I have a folder named data with my kaggle dataset. 
'jupyter-tensorflow-notebook' is my Docker container image name. I already have a folder in my docker 
container also named data where I am copying the file contents to. 

##### .oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.
