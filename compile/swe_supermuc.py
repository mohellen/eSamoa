target='release'
assertions=True
scenario='swe'
flux_solver='aug_riemann'
compiler='gnu'
#if enable iMPI, OpenMP must be disabled
openmp='noomp'
mpi='default'
impi='yes'
#asagi on/off switch: accept True or False
asagi=True
#use this asagi directory when using iMPI
asagi_dir='/home/hpc/h039w/di29zaf2/ihpc_workspace/libasagi'