```python

```

## askgpt

**About**

This module uses the openai API to ask for python code. It is a cheaper (for now and conditional on volume) alternative to GitHub copilot. If you are in a jupyter notebook it will insert the code in an appended cell. If you are in a python script it will append the code below.

To use it you first need to go here: https://platform.openai.com/docs/overview and create an account. Within the account create an API key. In my account I have an upper limit on the amount to spend per month. The website gives you a way to monitor your consumption.

**Setup**

Keep your credentials in a file (e.g. in the same folder as this code) named .env.openai which might look like this:

```
OPEN_AI_TOKEN=sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

**Use it so**

In any python file you are coding add these line on top:

```python
from dotenv import dotenv_values
config = dotenv_values(".env.openai")  
import askgpt
ask = askgpt.AUTH(config['OPEN_AI_TOKEN'])
```

any time you need assistance during coding just ask:

```python
ask.ai("Python code to load a csv file into  pandas")
```
he output will look kind of like this:

```
	#chagpt says 
	import pandas as pd

	# Load CSV file into a Pandas DataFrame
	df = pd.read_csv('data.csv')

	# Print the DataFrame
	print(df)
```
