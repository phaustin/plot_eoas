import matplotlib.pyplot as plt
from netCDF4 import Dataset
from matplotlib.colors import Normalize
from matplotlib import cm

def get_values(limit_dict,var_name,plot_var):
    """
       get title and units from the netcdf plot_var attributes
       git min and max if they exist from limit_dict, otherwise
           assign the_norm=None
    """
    the_norm=None
    if var_name in limit_dict:
        the_norm=Normalize(vmin=limit_dict[var_name]['varmin'],vmax=limit_dict[var_name]['varmax'],clip=False)
    title=plot_var.long_name
    units=plot_var.units
    return title,units,the_norm

data_file='/tera/phil/bomex_cmake/OUT_STAT/BOMEX_64x64x75_100m_40m_2s.nc'

nc_set=Dataset(data_file)

limit_dict={'TKE':{'varmin':0,'varmax':0.1},\
             'QC':{'varmin':0,'varmax':0.02},\
             'QV':{'varmin':0,'varmax':20}}


varname='QC'
varname='QCCLD'
height=nc_set.variables['z'][...]
plot_var=nc_set.variables[varname]
plot_field=plot_var[...]
time=nc_set.variables['time'][...]


title,units,the_norm=get_values(limit_dict,varname,plot_var)


cmap=cm.bone
cmap.set_over('r')
cmap.set_under('b')

fig=plt.figure(1)
fig.clf()
axis1=fig.add_subplot(111)
im=axis1.pcolormesh(time,height,plot_field.T,cmap=cmap,norm=the_norm)
cb=plt.colorbar(im,extend='both')
title="{0:s} ({1:s})".format(title,varname)
colorbar="{0:s} {1:s}".format(varname,units)
the_label=cb.ax.set_ylabel(colorbar,rotation=270)
axis1.set_xlabel('time (days)')
axis1.set_ylabel('height (m)')
axis1.set_title(title)
fig.canvas.draw()
plt.show()
