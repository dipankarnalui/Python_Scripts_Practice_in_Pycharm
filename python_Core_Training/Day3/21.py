import logging as log

#change the default logging level to DEBUG
#logging.basicConfig(level = logging.DEBUG)

#change the default logging level to DEBUG
#logging.basicConfig(level = logging.DEBUG, filename="err.logging")


#change the default logging level to DEBUG
log.basicConfig(level=log.DEBUG,filename="err.log",
               format="%(message)s %(asctime)s" )

log.debug("error-1")     # debug is 10 >= default level is 30
log.info("error-2")
log.warning("error-3")
log.error("error-4")
log.critical("error-5")