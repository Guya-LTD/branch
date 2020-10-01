# -*- coding: utf-8 -*-

"""Copyright Header Details

Copyright
---------
    Copyright (C) Guya , PLC - All Rights Reserved (As Of Pending...)
    Unauthorized copying of this file, via any medium is strictly prohibited
    Proprietary and confidential

LICENSE
-------
    This file is subject to the terms and conditions defined in
    file 'LICENSE.txt', which is part of this source code package.

Authors
-------
    * [Simon Belete](https://github.com/Simonbelete)
 
Project
-------
    * Name: 
        - Guya E-commerce & Guya Express
    * Sub Project Name:
        - Branch Service
    * Description
        - Branch location and details service
"""


from flask_restplus import Namespace, fields

from branch.blueprint.v1.branch import namespace


class BranchDto:
    """Request and Respons Data Transfer Object."""

    Language = namespace.model('Language', {
        'en': fields.String(required = True),
        'am': fields.String()
    })

    Location = namespace.model('Location', {
        'woreda': fields.String(),
        'kebele': fields.String(),
        'house_no': fields.String()
        #'gps': fields.String()
    })

    request = namespace.model('branch_request', {
        'names': fields.Nested(Language),
        'location': fields.Nested(Location),
        'manager_id': fields.String()
    })

    response = namespace.model('branch_response', {})