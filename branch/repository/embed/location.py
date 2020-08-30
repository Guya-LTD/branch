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


"""Package details

Application features:
--------------------
    Python 3.7
    Flask
    PEP-8 for code style


Entity.
"""

from branch.database import db


class Location(db.EmbeddedDocument):
    """Embedded document.
    
    Attributes
    ----------
    woreda : String

    kebele : String

    house_no : String

    gps : PointField
    """

    NEW = 'new'

    OLD = 'old'

    STATUS = (NEW, OLD)

    woreda = db.StringField()

    kebele = db.StringField()

    house_no = db.StringField()

    gps = db.PointField(auto_index=False)

    STATUS = db.StringField(choices = STATUS, default = NEW)