import phoebe
import pluginexample

logger = phoebe.logger(clevel='INFO')

b = phoebe.default_binary()

b.add_compute('customcompute')
b.add_dataset('lc', times=[0,1,2,3])
b.add_dataset('rv', times=[0,1,2,3])
b.run_compute()

print b['fluxes@model']
print b['rvs@primary@model']

