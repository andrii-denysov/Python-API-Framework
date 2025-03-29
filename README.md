# Python-API-Framework
This framework has been created for testing API of [PoetryDB](https://github.com/thundercomb/poetrydb#readme) application.
## Setup Your Working Enviorment with terminal or CLI

* git clone
* cd to project directory 
* Install virtualenv:
```
py -m pip install --user virtualenv
```
* Create a virtual environment: 
```
py -m venv testenv
```
* Activate your virtual environment:
```
.\testenv\Scripts\activate
```
* install project dependencies using pip: 
```
pip install -r requirenments.txt
```
## Setup work environment using IDE PyCharm
* download code as zip file from [Git](https://github.com/andrii-denysov/Python-Selenium-Pytest)
* Extract and open with Pycharm
* venv and dependencies will automatically setup and installed with notified pop-ups

## Run Tests

* Run according to tags:
```
pytest -k "<tag_name>" (e.g. pytest -k "smoke")
```

## Test cases
| Test Case ID | Description                                                  | Steps                                                                                                                                                                                                                              | Expected Result                                                                                                                                                                                                                                                                                             |
|--------------|--------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TC_001       | Verify user can search a poem by its title and author's name | 1. Send GET request to https://poetrydb.org/ endpoint with `author` and `title` parameters (e.g. https://poetrydb.org/author,title/William Shakespeare;Sonnet 1: From fairest creatures we desire increase)<br/>2. Verify response | Status code should be `200`.<br/>The response should be a valid JSON object.<br/>The JSON object should be an array of objects, each containing the following fields: `title`, `author`, `lines`, and `linecount`.<br/>The response should include a specific poem that matches the given `author` and `title`. |
| TC_002       | Verify user can find a poem that contains specified word     | 1. Send GET request to https://poetrydb.org/lines/{lines_to_search} endpoint (e.g. https://poetrydb.org/lines/nebula) <br/>2. Verify response                                                                                      | Status code should be `200`.<br/>The response should be a valid JSON object.<br/>The JSON object should be an array of objects, each containing the following fields: `title`, `author`, `lines`, and `linecount`.<br/>Every poem in the response must include the searched word (e.g., `nebula`) in at least one of its lines. |