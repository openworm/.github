import collections

owrefs = collections.OrderedDict()
otherrefs = collections.OrderedDict()

workflows = {}

def add_repo(name, path, wfs=None):
    owrefs[name] = path
    if wfs is not None:
        workflows[name] = wfs

owrefs['OpenWorm Docker'] = 'openworm/OpenWorm'
workflows['OpenWorm Docker'] = ['docker-image.yml', 'docker-image-quickrun.yml']

add_repo('c302', 'openworm/c302', ['ci.yml', 'non_omv.yml'])

add_repo('Sibernetic', 'openworm/sibernetic', ['ci-build.yml'])

add_repo('owmeta', 'openworm/owmeta', ['scheduled-master-build.yml', 'scheduled-dev-build.yml', 'dev-test.yml'])


add_repo('Hodgkin Huxley Tutorial', 'openworm/hodgkin_huxley_tutorial', ['omv-ci.yml', 'non-omv.yml'])

add_repo('Muscle model', 'openworm/muscle_model', ['omv-ci.yml', 'non-omv.yml'])

add_repo('NeuroPAL', 'openworm/NeuroPAL', ['omv-ci.yml', 'test-notebooks.yml'])


add_repo('Blender2NeuroML', 'openworm/Blender2NeuroML', ['ci-test.yml'])


add_repo('C elegans Neuromechanical Gait Modulation', 'OpenSourceBrain/CelegansNeuromechanicalGaitModulation', ['build.yml'])
add_repo('2D worm body model', 'openworm/CE_locomotion', ['ci-make.yml'])

otherrefs['NeuroML Documentation'] = 'NeuroML/Documentation'
workflows['NeuroML Documentation'] = ['prs.yaml', 'publish.yml']

otherrefs['OMV'] = 'OpenSourceBrain/osb-model-validation'
otherrefs['neuroConstruct'] = 'neuralensemble/neuroConstruct'
otherrefs['NeuroML 2'] = 'NeuroML/NeuroML2'
otherrefs['pyNeuroML'] = 'NeuroML/pyNeuroML'
