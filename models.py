# -*- coding: utf-8 -*-
from leancloud import Object

__author__ = 'pan'


class ZhuangBiRecord(Object):
    @property
    def ldl_id(self):
        return self.get('ldl_id')

    @property
    def steps(self):
        return self.get('steps')
