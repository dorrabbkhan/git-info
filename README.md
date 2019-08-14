# GitSizeViewer

 

Python script to view the size of a github repository, along with other useful information. This uses the requests and regex module to parse an input repository's URL, obtain the JSON for the respective repository using the Github API, parse the JSON, and display useful information about the Github repository. 





## How to run



If you haven't already, install the requests module using:

```
pip install requests
```

or

```
pip install -r requrements.txt
```



Download gitinfo.py, and execute the file in Python. Input the Github repository's URL, and the repository's name, owner's name, description, whether it is forked or not, size, and programming language will be displayed.


## Example usage




```
Enter url of repo: https://github.com/dorrabbkhan/demo

Name: demo
Owner: dorrabbkhan
Description: This is a demo repository
Is Forked: False
Size: 0.002 MB
Language: None
```

## Future plans





- Add a GUI
- Add support for more detailed information
- Implement on the web
- Turn into a reusable package instead of a script and publish package
- Write tests for the code


------



Feel free to suggest changes, and to fork! :)
