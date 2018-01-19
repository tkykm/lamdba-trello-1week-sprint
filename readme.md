# trello-1week-sprint

This is lamdba function that move all cards on progress lists to backlog list and archive all cards on done list every sunday.

## how to deploy to aws

First, configure env varibale.  
Please copy config.json.sample to config.json and edit it.
You can generate trello keys at https://trello.com/1/appKey/generate
```
    "TRELLO_KEY": "<your trello key>",
    "TRELLO_SECRET": "your trello secret",
    "TRELLO_BOARD": "<your trello board id>",
    "TRELLO_LIST_DONE": "<your kind of done list id>",
    "TRELLO_LIST_DONE": "<your kind of backlog list id>",
    "TRELLO_LISTS_PROGRESS": "<your kind of progress lists. you can specify multi ids by using ':' e.g. id1:id2:id3>" 
```

```
$ npm install -g serverless # if you have not installed serverless framework
$ aws login
$ npm install
$ sls deploy # docker required
```
