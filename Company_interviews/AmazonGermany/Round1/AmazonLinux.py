# Imagine your electricity utility company is not charging a fixed rate but an hourly.
# So every hour there is a different price. You get a list of the hourly electricity
# prices for the next 24 hours from the electricity company as json file. Write a tool,
# that calculates the cheapest price for a time frame given in hours (e.g. 3).

prices = {
    "16-17": 0.18, 
    "17-18": 0.23, 
    "18-19": 0.26, 
    "19-20": 0.27,
    "20-21": 0.27,
    "21-22": 0.12,
    "22-23": 0.07,
    "23-0": 0.02,
    "0-1": 0.01,
    "1-2": -0.04,
    "2-3": -0.10,
    "3-4": 0.00,
    "4-5": 0.10,
    "5-6": 0.20,
    "6-7": 0.23,
    "7-8": 0.32,
    "8-9": 0.27,
    "10-11": 0.25,
    "11-12": 0.30,
    "12-13": 0.29,
    "13-14": 0.24,
    "14-15": 0.22,
    "15-16": 0.19
}

duration = 3 # hours

# Expected result: Start time 1-2 End time 3-4



##Write your code here =>

#d1.sort(values)
#top3 - lowest prices 
#index of those top3 
#indexes are adjacent, then print the the first and third lowest  

key_list=prices.keys()

d2=[]
for i in range(len(key_list)):
    sum=prices[key_list[i]] + prices[key_list[i+1]] + prices[key_list[i+2]]
    d2[prices[key_list[i]]]=sum
    
d2={"start1":5,
    "start2":3,
    "start3":1,
}

d2.sort(value) #sort of dict by values 


d2={"start3":1,
    "start2":3,
    "start1":5,
}
    
d2[0]    

#use a for loop to get the third index from the start to get the end hours 