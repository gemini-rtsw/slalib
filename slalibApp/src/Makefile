TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#=============================
# Build a support module called <APPNAME>

LIBRARY_IOC += slalib

# <APPNAME>.dbd will be created and installed
DBD += slalib.dbd

# slalib.dbd will be made up from these files:
slalib_DBD += base.dbd
# List local .dbd files here
# slalib_DBD += xxx.dbd

# Include dbd files for external support modules:
# slalib_DBD += genSubRecord.dbd

# specify all source files to be compiled
# including sequencer (.st) source files
#slalib_SRCS += xxx.c
#slalib_SRCS += xxx.st

#=============================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

