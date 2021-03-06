#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 UWATC. All rights reserved.
#
# Use of this source code is governed by an MIT license that can
# be found in the LICENSE.txt file or at https://opensource.org/licenses/MIT

# TODO: refactor into factory function

import datetime as _datetime

from data import DataEnums
from data import DataRaw
from data import OrderType

from data.augmenters import SimpleAugmenter

from agent import SimpleAgent

def test_agent():
	dict_ts = _datetime.time(12, 30, 12)
	data_obj = DataRaw(OrderType.CONTINOUS, [{"timestamp": dict_ts}])
	augmented = SimpleAugmenter([data_obj])
	agent = SimpleAgent([data_obj, augmented])