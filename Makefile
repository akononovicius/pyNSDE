CC = gcc

SRC_DIR = src

LINKER_FLAGS = -lgsl -lgslcblas
OBJ_C_FLAGS = -c -fpic
OBJ_SO_FLAGS = -shared -o

all: libsde.so

#
# SHARED OBJECTS
#
libsde.so: sde.o
	${CC} ${OBJ_SO_FLAGS} libsde.so sde.o ${LINKER_FLAGS}

#
# COMPONENT OBJECTS
#
sde.o: ${SRC_DIR}/sde.c ${SRC_DIR}/sde.h
	${CC} ${OBJ_C_FLAGS} ${SRC_DIR}/sde.c ${LINKER_FLAGS}

#
# GENERAL CMDS
#
clean:
	rm *.o

# vim: set noexpandtab tabstop=4 shiftwidth=4 softtabstop=-1:
