#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 UWATC. All rights reserved.
#
# Use of this source code is governed by an MIT license that can
# be found in the LICENSE.txt file or at https://opensource.org/licenses/MIT

class Wallet:
    def __init__(self, crypto_amount):
        self.crypto_amount = crypto_amount
        self._reserved = 0.0