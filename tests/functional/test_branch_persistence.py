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
"""

import pytest
from faker import Faker

from branch.repository.embed import Names, Location
from branch.repository.branch import Branch

class TestBranchRepository:

    AM_WORD_LIST = (
        'አልማዝን', 'አየኋት', 'ከፈትኩላት', 'በሩን', 'ዘጋሁባት',
        'አየሩ', 'ተኝቷል', 'ኢትዮጵያ', 'ውስጥ', 'ናት', 'ከተማ'
    )

    def setup_class(self):
        # init faker object
        self.faker = Faker()
        #self.gps = {
        #    'type': 'Point',
        #    'coordinates': [self.faker.coordinate(), self.faker.coordinate()]
        #}
        self.gps = [-15, -47] #[self.faker.coordinate(), self.faker.coordinate()]
        self.names = Names(
            en = self.faker.sentence(),
            am = self.faker.sentence(ext_word_list = self.AM_WORD_LIST)
        )
        self.location = Location(
            woreda = self.faker.country_code(),
            kebele = self.faker.postcode(),
            house_no = self.faker.building_number(),
            # latitude, longitude
            gps = self.gps
            sdf
        )
        self.branch = Branch(
            names = self.names,
            location = self.location,
            manager_id = self.faker.name()
        )

    def test_branch_object_creation(self):
        #self.branch.save()
        #assert branch.id != None
        pass