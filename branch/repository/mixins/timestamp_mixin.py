
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
        - Catalog Service
    * Description
        - Catlog Catalog Service
"""


"""Package details

Application features:
--------------------
    Python 3.7
    Flask
    PEP-8 for code style
    flask-mongoengine v0.7


flask-mongoengine based ODM flask-mongoengine built up on pymongo engine.
"""

from datetime import datetime
from pytz import timezone

from branch.database import db


class TimestampMixin():
    """Time Stamped Mixin

    Attributes
    ----------
    created_at : DateTime

    updated_at : DateTime
    """

    created_at = db.DateTimeField(default = datetime.now(timezone('Africa/Addis_Ababa')))

    updated_at = db.DateTimeField(default = datetime.now(timezone('Africa/Addis_Ababa')))