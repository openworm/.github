
from RepoInfo import *
import os

info = """
## Tests on OpenWorm active repositories
"""

count = 0


allrefs = {'Core OpenWorm': owrefs,
           'Documentation': owdocs,
           'Related repositories': otherrefs,}

for cat in allrefs:
    info += '\n### %s\n\n'%cat

    info += '| Repository | Tests | Tests (development) | PRs |\n'
    info += '|----------|:------:|:------:|:------:|\n'

    refs = allrefs[cat]
    for name in refs.keys():
        ref = refs[name]
        summary = summaries[name] if name in summaries else ""

        print("Looking at: %s in %s"%(ref, name))

        info += '| <a href="https://github.com/%s">%s</a><br/><i><sup>%s</sup></i> |'%(ref,name,summary)

        wfs = ['ci.yml'] if not name in workflows else workflows[name]
        dev = ''
        for wf in wfs:
            info += '  [![OMV](https://github.com/%s/actions/workflows/%s/badge.svg)](https://github.com/%s/actions/workflows/%s) '%(ref,wf,ref,wf)
            if 'pages' in wf:
                dev += '-'
            else:
                dev += '  [![OMV](https://github.com/%s/actions/workflows/%s/badge.svg?branch=development)](https://github.com/%s/actions/workflows/%s) '%(ref,wf,ref,wf)

        info += '  | %s |'%dev

        info += '  [![GitHub pull requests](https://img.shields.io/github/issues-pr/%s)](https://github.com/%s/pulls) | \n'%(ref,ref)


        count+=1

info += '  </table>\n'


readme = open('README.md','w')
readme.write(info)
readme.close()
