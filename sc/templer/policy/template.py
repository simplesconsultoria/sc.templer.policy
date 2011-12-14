# -*- coding:utf-8 -*-
import copy

from templer.core.base import get_var
from templer.core.vars import EXPERT
from templer.core.vars import BooleanVar

from sc.templer.core.base import PlonePackage

from sc.templer.core.utils import gen_version


class PortalPolicy(PlonePackage):

    summary = "A policy package following the Simples Consultoria standards"
    help = "A package that will manage a Plone installation"

    category = "Simples Consultoria - Plone"

    _template_dir = "templates/policy"
    vars = copy.deepcopy(PlonePackage.vars)

    vars.append(
        BooleanVar(
            'add_profile_init_content',
            title='Register an Initial Content Profile',
            description='''Should this package register an Initial
                           Content GS Profile ''',
            modes=(EXPERT, ),
            default=True,
            structures={'False': None, 'True': 'gs_nested_init_content'},
        ),
    )

    get_var(vars, 'version').default = gen_version()
    get_var(vars, 'add_profile').structures ={'False': None,
                                              'True': ['gs_nested_default',
                                                       'gs_nested_policy']}
