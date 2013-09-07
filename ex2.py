import sched, time
 
def hello(name):
    print 'hello world, i am %s, Current Time:%s' % (name, time.time())
    run(name)
    
def run(name):
    s = sched.scheduler(time.time, time.sleep)
    s.enter(3, 2, hello, (name,))
    s.run()
    
s = sched.scheduler(time.time, time.sleep)
s.enter(3, 2, hello, ('Tom',))
s.run()
