# Changelog



All notable changes/additions/deletions are documented in this file.



## 16 Aug, 2019



### Changes

- Wrote further unittests for the values returned by the Repository class methods
- Formatted the unittests better
- Implemented assertIs instead of assertIsInstance for tighter check on types of data returned
- Removed redundant int() functions on returned values in some of the Repository class methods since data returned by the Github API's JSON is already int
- Added checks for incorrect URL's to test.py
- Added check for when a data type other than string is passed to the Repository class's init function



## 15 Aug, 2019



### Additions

- Added changelog file
- Added an informal test file 
- Added .gitignore for .pyc files



### Changes

- Major refactoring on the code on the refactoring branch, turned into a reusable Python package
- Implemented OOP by adding a Repository class 
- Retained and improved functionality (more detailed information about the repository) when the code is run as a script in itself
- Implemented slightly better error handling
- Updated readme
- Fixed issue #1 - added support for repository names with _ in them
- Wrote unittests for regex pattern checks with correct URL inputs