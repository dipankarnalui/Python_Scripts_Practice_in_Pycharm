import logging as log

#change the default log level to DEBUG
#log.basicConfig(level = log.DEBUG) # now default level 10
log.basicConfig(level = log.DEBUG, filename="err.log")

log.debug("error-1") # debug is 10>=30 default level is 30
log.info("error-2") # info is 20>=30
log.warning("error-3") # warning is 30>=30
log.error("error-4") # error is 40>=40
log.critical("error-5") # critical is 50>=50

