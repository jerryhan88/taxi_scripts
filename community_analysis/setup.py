from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension("b_group._cy_b1_influenceGraph", ["b_group/_cy_b1_influenceGraph.pyx"], include_dirs=['.']),
]

setup(
    name='taxi_projects',
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules,
    script_args=['build_ext'],
    options={'build_ext': {'inplace': True, 'force': True}}
)

print '********CYTHON COMPLETE******'