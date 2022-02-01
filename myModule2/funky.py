import logger
log = logger.get_logger(__name__)

# start from here 
def divbyz(a,b):
    """[This function generates a divison of two numbers]

    Args:
        a ([number]): [Nominator]
        b ([number]): [denominator]
    """
    log.info (" This is the start of divideby function and I am trying to enter %s and %s",a,b)
    try:
        div=a/b
        log.info(" Executed sucessfully")
    except Exception as e:
        log.error(" Error has happened")
        log.exception(" Exception occures " + str(e))