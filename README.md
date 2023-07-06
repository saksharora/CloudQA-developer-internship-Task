# CloudQA-developer-internship-Task
This project contains a Python script using Selenium to automatically test three fields on the CloudQA Automation Practice Form.
Table of Contents
Installation
Usage
Contributing
License
Installation
To run the script, you will need to have Python and Selenium installed on your system. You can install them using pip:
sh
Copy
pip install selenium
You will also need to download the appropriate driver for your browser. The script is currently set up to use the Firefox driver, but you can easily modify it to use another driver. You can download the Firefox driver from the official Mozilla GitHub repository.
Usage
To run the script, simply execute the test_fields.py file using Python:
sh
Copy
python test_fields.py
The script will automatically navigate to the CloudQA Automation Practice Form, enter a test value into each of the first name, last name, and email fields, and verify that the value was entered correctly. If any errors occur during the test, the script will print an error message.
Contributing
If you find any issues with the script or would like to suggest improvements, feel free to create a pull request or open an issue. We welcome contributions from anyone!

