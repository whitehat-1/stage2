from fastapi import FastAPI 

app = FastAPI()


db = [
    {'name':'jerry', 'address':'lagos'},  
    {'name':'sandra', 'address':'abuja'},  
    {'name':'precious', 'address':'Uyo'},   
]

#<--This is the edpoint that accepts a path parameter

@app.get('/items/')  
async def stage_two():
    return{'Hello': 'Welcome to Kodecamp intermediate stage 2'}
     

@app.get('/stage2/') 
async def stage_two():
    return{'Hello jerry': 'Welcome to Kodecamp intermediate stage 2'}
  
@app.get('/stage2/{index}')    
async def stage_two(index: int): 
    return{'Hello':[index]} 
#<--The value of the path parameter index will be passed to your function as the argument index.


#<- This is the endpoint  that accepts a query parameter
@app.get("/stage2/")   
async def stage_two(name: str):
    return{'Hello jerry':[name]} 


## Example query parameter input below:
# http://127.0.0.1:8000/stage2/?name="welcome to kodecamp stage 2"
#? ==> pass the query
#name ==> pass the value of the path parameter and the message
 