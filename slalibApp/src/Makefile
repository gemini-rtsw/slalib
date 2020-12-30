TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#==================================================
# build a support library

LIBRARY_IOC += slalib

# xxxRecord.h will be created from xxxRecord.dbd
#DBDINC += xxxRecord
# install slalib.dbd into <top>/dbd
DBD += slalib.dbd

# specify all source files to be compiled and added to the library
SRCS.c    = $(wildcard ../*.c)
slalib_SRCS += $(strip $(patsubst ../%.c,    %.o, $(SRCS.c)))

INC += slalib.h
INC += slamac.h

slalib_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

