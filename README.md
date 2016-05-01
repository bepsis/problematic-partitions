# Problematic Partitions
![woah](http://puu.sh/oCNSS/f758d835e8.png)
Exploring approximations of [Ramanujan](https://en.wikipedia.org/wiki/Srinivasa_Ramanujan)'s deceptively simple [partition function](http://mathworld.wolfram.com/PartitionFunctionP.html).

Using polynomial linear regression, one can train a regressor to generate a function which is pretty accurate, and is also really fast. Below is a graph showing how Ramanujan's approximation function (green), the actual partition function (blue), and my approximation (red) compare.

![comparison](http://puu.sh/oCMQQ/b088085215.png)

As you can see, the regressor's function is pretty accurate, but we could do even better if we had more training points to learn from in the actual function (the partition function grows at an amazingly fast exponential rate, and the regressor is only trained on a tiny slice of the function).

### Installation
To hack or test this script yourself (or try and train the regressor's function with more data points -- I couldn't due to lack of proper computing power), install Python 3.4+ and run the following commands (I prefer to do so within a virtualenv, but if that's not your thing, no worries):
```shell
$ pip install -r requirements.txt
```
Run the script:
```
$ python ramanujan.py
```
