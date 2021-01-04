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
from branch.model.branch import Branch as BranchEntity
from .embed.names import Names
from .embed.location import Location
from .mixins.timestamp_mixin import TimestampMixin
from .mixins.user_mixin import UserMixin

class Branch(db.Document, BranchEntity, TimestampMixin, UserMixin):
    """Branchs ODM

    ...

    Attributes
    ----------
    _id : String 
        Auto inherated attribute, 12-byte, 24 char hexadicmal

    names : Dictionary
        Language Translation References, called with their short name
        Example :
            - names.en
            - names.am

    manager_id : String
        User id

    status : String
        Acive in use or closed
    """

    OPEN = 'open'

    CLOSED = 'closed'

    STATUS = (OPEN, CLOSED)

    COMPANY = ("shop", "xpress")

    names = db.EmbeddedDocumentField(Names)

    manager_id = db.StringField()

    status = db.StringField(choices = STATUS)

    location = db.EmbeddedDocumentField(Location)

    company = db.StringField(choices = COMPANY)