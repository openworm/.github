import collections

owrefs = collections.OrderedDict()
otherrefs = collections.OrderedDict()

workflows = {}
summaries = {}

def add_repo(name, path, wfs=None, info=None):
    owrefs[name] = path
    if wfs is not None:
        workflows[name] = wfs
    if info is not None:
        summaries[name] = info
    

owrefs['OpenWorm Docker'] = 'openworm/OpenWorm'
workflows['OpenWorm Docker'] = ['docker-image.yml', 'docker-image-quickrun.yml']
summaries['OpenWorm Docker'] = 'Repository for the main Dockerfile with the complete OpenWorm software stack. Also hosts project-wide issues.'

add_repo('c302', 'openworm/c302', ['ci.yml', 'non_omv.yml'], 'The c302 framework for generating multiscale network models of C. elegans')

add_repo('Sibernetic', 'openworm/sibernetic', ['ci-build.yml'], "A C++/OpenCL implementation of the PCISPH algorithm supplemented with a set of biomechanics related features applied to C. elegans locomotion")

add_repo('owmeta', 'openworm/owmeta', ['scheduled-master-build.yml', 'scheduled-dev-build.yml', 'dev-test.yml'], 'Unified, simple data access python library for data & facts about C. elegans anatomy')


add_repo('Hodgkin Huxley Tutorial', 'openworm/hodgkin_huxley_tutorial', ['omv-ci.yml', 'non-omv.yml'], 'A repository containing code for a number of tutorials on the Hodgkin Huxley model, including an interactive Jupyter notebook')

add_repo('Muscle model - Boyle & Cohen 2008', 'openworm/muscle_model', ['omv-ci.yml', 'non-omv.yml'], 'Model of C. elegans body wall muscle based on Boyle & Cohen 2008')

add_repo('Muscle model - Johnson & Mailler 2015', 'openworm/JohnsonMailler_MuscleModel', ['omv-ci.yml', 'non-omv.yml'], 'C. elegans muscle model from Johnson & Mailler 2015')


add_repo('NeuroPAL', 'openworm/NeuroPAL', ['omv-ci.yml', 'test-notebooks.yml'], 'Scripts to analyse and convert NeuroPAL datasets')


add_repo('Blender2NeuroML', 'openworm/Blender2NeuroML', ['ci-test.yml'], 'Conversion script to bring neuron models created in Blender into NeuroML format')


add_repo('C. elegans Neuromechanical Gait Modulation', 'OpenSourceBrain/CelegansNeuromechanicalGaitModulation', ['build.yml'], 'C. elegans neuromechanical gait modulation model from Boyle, Berri and Cohen 2012')
add_repo('2D worm body model', 'openworm/CE_locomotion', ['ci-make.yml'], 'Neuromechanical model of locomotion in C. elegans, originally developed by Eduardo Izquerdo, Erick Olivares and Randall Beer')

otherrefs['NeuroML Documentation'] = 'NeuroML/Documentation'
workflows['NeuroML Documentation'] = ['prs.yaml', 'publish.yml']

otherrefs['OMV'] = 'OpenSourceBrain/osb-model-validation'
otherrefs['neuroConstruct'] = 'neuralensemble/neuroConstruct'
otherrefs['NeuroML 2'] = 'NeuroML/NeuroML2'
otherrefs['pyNeuroML'] = 'NeuroML/pyNeuroML'
