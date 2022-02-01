import logger
log = logger.get_logger(__name__)

# start from here 

def multiply(num1, num2):
    log.debug("Executing the multiply function.")
    return num1 * num2

def divby(a,b):
    log.info (" This is the start of divideby function and I am trying to enter %s and %s",a,b)
    try:
        div=a/b
        log.info(" Executed sucessfully")
    except Exception as e:
        log.error(" Error has happened")
        log.exception(" Exception occures " + str(e))



        