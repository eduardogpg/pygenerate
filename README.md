### PyNumbat

__PyNumbat__ is a Python project generator. Easy to install and easy to use.

Files and folders to be created in the initial setup:

```
root/
│
├── env/
├── app/
│   ├── config.py
│   ├── __init__.py
│   ├── __main__.py
│
├── tests/
│   ├── test.py
│
├── README.md
├── .gitignore
└── main.py
```

### Commands

With a couple flags you can create a basic and functional setup for your python projects.  🐍


```python
pynumbat -p <Path>

```

If a previous python setup exists, you can overwrite it. This action will delete all files and folders previously existing

```python
pynumbat -p <Path> -f true
```

Optional, you can ommit the virtual env folder.

```python
pynumbat -p <Path> -f true -v false
```

It is important to note that, by default __Pynumbat__ takes the current version of Python on your machine to create the virtual environment.

