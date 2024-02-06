alst = [
        "ravi",
        "hari",
        "manoj",
        "yashasvi",
        "guru"
       ]
#Expected:- #newlst = ["ri", "hi", "mj", "yi", "gu"]
output = list(map(lambda x : x[0] + x[-1], alst))
print(output)