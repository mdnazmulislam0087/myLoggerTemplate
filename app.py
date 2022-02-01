import logger
log=logger.setup_applevel_logger(file_name='loggerfile.log')

import myModule
import myModule2

log.debug("Calling myModule")
# Here are the codes


myModule.multiply(9, 8)
myModule.divby(5,0)



# Finish line
log.debug("Finished module")

log.debug("Calling myModule2")
myModule2.divbyz(4,0)

log.debug("Finished myModule2")
