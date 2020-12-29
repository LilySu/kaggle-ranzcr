##### .oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.

## Cleanup
#### Stop One Container
```
docker stop <CONTAINER_ID>
```
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

##### .oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.
