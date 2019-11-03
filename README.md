## Android app Automation using appium, python and behave module 

### Installation
+ Install python
```
brew install python
```
+ Install appium
```
brew install node
npm install -g appium
```
+ Install dependencies
```
pip install -r requirements.txt
```
+ Download and install instagram on your android device
+ Set username and password for instagram
```
├──steps/welcome_steps.py
username = "your_username"
password = "your_password"
```

### Create page objects:
+ Base screen 
+ Login screen
+ Welcome screen

### Test cases:
+ Login

### Repository tree
```
.
├── pages
│   └── base_screen.py
│       ├── welcome_screen.py
│       └── login_screen.py
├── steps
│   ├── basic_steps.py
│   └── welcome_steps.py
├── tests
│   └── login.feature
├── requirements.txt
└── README.md
```

### Run

+ Start appium server from command line
```
appium
```
+ cd to /features folder and execute
```
behave
```