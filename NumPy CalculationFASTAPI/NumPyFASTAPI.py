from fastapi import FastAPI 
import numpy as np

app=FastAPI()
numbers = np.array([10, 20, 35, 43, 50, 69, 70, 81, 90])


#GET /numbers
@app.get("/numbers")
def get_numbers():
    return {"numbers":numbers.tolist()}

#GET /mean
@app.get("/mean")
def get_mean():
    return {"mean" :float(np.mean(numbers))}

#GET /median
@app.get("/median")
def get_median():
    return {"median" :float(np.median(numbers))}

#GET /std
@app.get("/std")
def get_std():
    return {"std" :float(np.std(numbers))}

#GET /variance
@app.get("/variance")
def get_variance():
    return {"variance" :float(np.var(numbers))}

#GET /Maximum
@app.get("/Maximum")
def get_maximum():
    return {"Maximum" :(np.max(numbers))}

#GET /Minimum
@app.get("/Minimum")
def get_minimum():
    return {"Minimum" :(np.min(numbers))}

#GET /Sum
@app.get("/Sum")
def get_sum():
    return {"total" :(np.sum(numbers))}

#GET /even
@app.get("/even")
def get_even():
    even_numbers=numbers[numbers%2==0]
    return {"even_numbers" :even_numbers.tolist()}

#GET /odd
@app.get("/odd")
def get_odd():
    odd_numbers=numbers[numbers%2!=0]
    return {"odd_numbers" :odd_numbers.tolist()}

#GET /stats
@app.get("/stats")
def get_stats():
    return {"mean" :float(np.mean(numbers)),
            "median" :float(np.median(numbers)),
            "std" :float(np.std(numbers)),
            "variance" :float(np.var(numbers)),
            "Maximum" :(np.max(numbers)),
            "Minimum" :(np.min(numbers))}

#GET /table/15
@app.get("/table/{number}")
def multiplation(number:int):
    table=np.arange(1,11)*number
    return {
        "Number" : number,
         "table":table.tolist()
    }

