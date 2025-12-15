import logging as log

# change the default log level to DEBUG
# redirect the error message to the LOG FILE named - err.log

log.basicConfig(level = log.DEBUG, filename="err.log")

log.debug("mesg-1")
log.info("mesg-2")
log.warning("mesg-3")
log.error("mesg-4")
log.critical("mesg-5")




