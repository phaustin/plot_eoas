import matplotlib.pyplot as plt
from netCDF4 import Dataset
from matplotlib.colors import Normalize
from matplotlib import cm

def get_values(limit_dict,var_name,plot_var):
    """
       get title and units from the netcdf plot_var attributes
       git min and max if they exist from limit_dict, otherwise
           assign None
    """
    varmin,varmax=None,None
    if var_name in limit_dict:
        varmin,varmax=limit_dict[var_name]['varmin'],limit_dict[var_name]['varmax']
    title=plot_var.long_name
    units=plot_var.units
    return title,units,varmin,varmax

data_file='/tera/phil/bomex_cmake/OUT_STAT/BOMEX_64x64x75_100m_40m_2s.nc'

nc_set=Dataset(data_file)

limit_dict={'TKE':{'varmin':0,'varmax':0.1},\
             'QC':{'varmin':0,'varmax':0.02},\
             'QV':{'varmin':0,'varmax':20},\
             'CLDLOW':{'varmin':0.1,'varmax':0.21}}


varname='QC'
varname='QCCLD'
varname='CLDLOW'
plot_var=nc_set.variables[varname]
plot_field=plot_var[...]
time=nc_set.variables['time'][...]


title,units,varmin,varmax=get_values(limit_dict,varname,plot_var)


fig=plt.figure(1)
fig.clf()
axis1=fig.add_subplot(111)
im=axis1.plot(time,plot_field)
title="{0:s} ({1:s})".format(title,varname)
axis1.set_xlabel('time (days)')
ylabel="{0:s} {1:s}".format(varname,units)
axis1.set_ylabel(ylabel)
axis1.set_title(title)
axis1.set_ylim((varmin,varmax))
fig.canvas.draw()
plt.show()
