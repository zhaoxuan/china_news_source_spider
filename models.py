#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright (C) 2016 JohnZ
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.
#

"""
models
"""

from peewee import *


DATABASE = MySQLDatabase('db_19', **{
    'host': '182.254.156.233',
    'user': 'user_19',
    'password': 'FdJb0cgf',
    'port': 3306,
})
DATABASE.connect()


class NewsSite(Model):
    class Meta:
        database = DATABASE

    id = PrimaryKeyField()
    dt = IntegerField(index=True)
    is_active = BooleanField(default=True)
    is_delete = BooleanField(default=False)
    create = IntegerField()
    update = IntegerField()
    domain = CharField(max_length=1024)
    name = CharField(max_length=128)


if __name__ == '__main__':
    NewsSite.create_table()
