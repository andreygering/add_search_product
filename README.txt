How to start server. 

Activate Virtual Environment MacOS.
Folder: andrew/add_search_product
Command: source virtenvmacos/bin/activate  

How to run project on flask 
Command: flask run -p 5002  (Port must to be 5002)

Activate Virtual Environment WindowsOS.
Folder: andrew/virtenvwin 
Command 1: (go to folder) cd andrew/virtenvwin/Scripts
Command 2: activate

How to run project on flask 

Back to add_search_product (folder)
Command: flask run -p 5002 (port must to be 5002)




SECURITY NOTES:

1. For full/really using I would use an https server.
2. All output from form enter to variablle and only the variable is placed in the SQL query.
3. All the queries using method POST on the POST method with ( HTTPS server) can encrypt the conten on the body it's help to save our query or result. 
