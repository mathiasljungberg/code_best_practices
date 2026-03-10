F90 =gfortran

LOPT=-llapack -lblas

LOBJS=splines.o\
spline_m.o\
KH_functions.o\

all: parameters spline_m KH_functions sinc_DVR

parameters: parameters.f90
	$(F90) $(F90FLAGS) -c parameters.f90

spline_m: spline_m.f90 parameters.f90
	$(F90) $(F90FLAGS) -c spline_m.f90

KH_functions: KH_functions.f90
	$(F90) $(F90FLAGS) -c KH_functions.f90

sinc_DVR: sinc_DVR.o $(LOBJS) 
	$(F90) $(LFLAGS) -o sinc_DVR sinc_DVR.o \
	$(LOBJS) $(LOPT)

%.o: %.f
	$(F90) $(F90FLAGS) -c $*.f

%.o: %.f90
	$(F90) $(F90FLAGS) -c $*.f90

clean: 
	rm -f *.o *.mod sinc_DVR

