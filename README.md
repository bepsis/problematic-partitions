# Problematic Partitions
Exploring approximations of [Ramanujan](https://en.wikipedia.org/wiki/Srinivasa_Ramanujan)'s deceptively simple [partition function](http://mathworld.wolfram.com/PartitionFunctionP.html).

Using polynomial linear regression, one can train a regressor to generate a function which is pretty accurate, and is also really fast. 

### Installation
To hack or test this script yourself (or try and train the regressor's function with more data points -- I couldn't due to lack of proper computing power), install Python 3.4+ and run the following commands (I prefer to do so within a virtualenv, but if that's not your thing, no worries):
```shell
$ pip install -r requirements.txt
```
Run the script:
```
$ python ramanujan.py
```


### Visualization
Here's a good way of understanding the simplicity and growth rate of the partition function:
![woah](http://puu.sh/oCNSS/f758d835e8.png)
