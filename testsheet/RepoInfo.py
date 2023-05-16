import collections

owrefs = collections.OrderedDict()
otherrefs = collections.OrderedDict()

workflows = {}
workflows['NeuroML Documentation'] = ['prs.yaml', 'publish.yml']

owrefs['OpenWorm Docker'] = 'openworm/OpenWorm'
workflows['OpenWorm Docker'] = ['docker-image.yml', 'docker-image-quickrun.yml']

owrefs['c302'] = 'openworm/c302'
workflows['c302'] = ['ci.yml', 'non_omv.yml']

owrefs['sibernetic'] = 'openworm/sibernetic'
workflows['sibernetic'] = ['ci-build.yml']


otherrefs['NeuroML Documentation'] = 'NeuroML/Documentation'

otherrefs['OMV'] = 'OpenSourceBrain/osb-model-validation'
otherrefs['neuroConstruct'] = 'neuralensemble/neuroConstruct'
otherrefs['NeuroML 2'] = 'NeuroML/NeuroML2'
otherrefs['pyNeuroML'] = 'NeuroML/pyNeuroML'
