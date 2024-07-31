import logging as log

#change the default log level to DEBUG
log.basicConfig(level=log.DEBUG, filename="err.log",
                format="%(levelname)s %(message)s %(asctime)s")
