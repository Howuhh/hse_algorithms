from  _continuation  import  continulet
def invoke(_, callable , arg):
    return callable(*arg)

def bootstrap(c):
    callable , *arg = c.switch()
    while  True:
        to = continulet(invoke , callable , arg)
        callable , *arg = c.switch(to=to)
cont = continulet(bootstrap)
cont.switch ()
