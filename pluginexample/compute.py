from phoebe.parameters import *
from phoebe import u

def customcompute(**kwargs):
    params = []

    params += [BoolParameter(qualifier='enabled', copy_for={'context': 'dataset', 'kind': ['lc', 'rv', 'orb'], 'dataset': '*'}, visible_if='False', dataset='_default', value=kwargs.get('enabled', True), description='Whether to create synthetics in compute/fitting run')]

    params += [FloatParameter(qualifier='someoption', value=kwargs.get('someoption', 0.01), default_unit=u.dimensionless_unscaled, description='blah')]

    return ParameterSet(params)