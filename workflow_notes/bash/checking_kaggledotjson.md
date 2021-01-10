Bash into Container

```docker exec -it kaggle-ranzcr_notebooks_1 /bin/bash```

```
nano kaggle.json
```
paste: {"username":"lsxsls","key":"6aad337fe3187f90f9c92dd7fde1ef90"}


```
nano check_kaggledotjson.sh
```
paste contents of check_kaggledotjson.sh
```
bash -f check_kaggledotjson.sh
rm -rf check_kaggledotjson.sh
```


notes:
```
# if kaggle.json in project home directory exists
# and grep returns exit 0 of match

if [[ -f ~/kaggle.json ]] && grep -q "^\{\"username\"\:|\,\"key\"\:|\"\}$" kaggle.json;
then
    printf "%s\n"  " " \ " <>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>" \ " " \ "   The kaggle.json is recognized to exist in this project directory." \ " " \ "                             ʕᵔᴥᵔʔ" \ " " \ "     You are ready to use the Kaggle CLI to download any dataset." \ " " \ " <>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>" \ " "

# if kaggle.json in project home directory exists

elif [[ -f ~/kaggle.json ]]
then
    printf "%s\n"  " " \ " <>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>" \ " " \ "   The kaggle.json is recognized to exist in this project directory." \ " " \ "                             ʕᵔᴥᵔʔ" \ " " \ "     However, your Kaggle API key is not in the correct format." \ " " \  "     Please make sure the content of the file matches this format:" \ "  {\"username\":\"<username>\",\"key\":\"********************************\"}" \ " " \ " <>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>--<>" \ " "

# if kaggle.json does not exist or is not named correctly
else
    printf "%s\n"  " " \ "<>--<>--<>--<>--<>--<>--<>--<>" \ "The kaggle.json does not exist in this project directory." \ "<>--<>--<>--<>--<>--<>--<>" \  " " \ "We offer two ways to use the Kaggle CLI" \ "which requires your Kaggle API key:"  \ "1. copy the contents of your kaggle.json one for one in the .env" \ "2. copy the file kaggle.json in the project directory prior to running docker-compose up " \ " " \ "Or if the data already exists in your local directory," \ "you can run a cp command (see README) to copy your local dataset into this container" \ "without interacting with the Kaggle CLI" \ " " \ "<>--<>--<>--<>--<>--<>--<>" \ " " \ "<>--<>--<>--<>--<>--<>--<>--<>" \ " "
fi
```