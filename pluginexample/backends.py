from phoebe.parameters import ParameterSet
from phoebe import u, c
from phoebe.backend.backends import _extract_from_bundle_by_dataset, _extract_from_bundle_by_time

import numpy as np

def customcompute(b, compute, times=[], **kwargs):
    """
    """

    # get the ParameterSet of just the compute options.  This will make it
    # much easier to access compute options than having to filter at the
    # bundle-level always.
    computeparams = b.get_compute(compute, force_ps=True)

    # Whenever retrieving a compute option, pass **kwargs to allow for
    # temporary overriding from run_compute
    someoption = computeparams.get_value('someoption', **kwargs)

    # Access hierarchy information
    hier = b.get_hierarchy()

    starrefs  = hier.get_stars()
    orbitrefs = hier.get_orbits()

    # Call either _extract_from_bundle_by_time or _extract_from_bundle_by_dataset
    infos, new_syns = _extract_from_bundle_by_dataset(b, compute=compute, times=times)

    # Now we can loop over infos and new_syns.  We need to fill and yield
    # the new_syns
    for info in infos:
        info = info[0]

        this_syn = new_syns.filter(component=info['component'], dataset=info['dataset'])

        if info['kind'] == 'lc':
            this_syn['fluxes'] = np.ones(info['times'].shape)
        elif info['kind'] == 'rv':
            this_syn['rvs'] = np.zeros(info['times'].shape)
        else:
            pass

    yield new_syns
