# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.transaction import Transaction

__all__ = ['SaleShop']


class SaleShop(metaclass=PoolMeta):
    __name__ = 'sale.shop'

    @classmethod
    def read(cls, ids, fields_names=None):
        # Skip access rule
        with Transaction().set_user(0):
            return super(SaleShop, cls).read(ids, fields_names=fields_names)
