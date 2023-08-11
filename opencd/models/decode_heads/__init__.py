from .bit_head import BITHead
from .changer import Changer
from .sta_head import STAHead
from .identity_head import IdentityHead, DSIdentityHead
from .tiny_head import TinyHead
from .ds_fpn_head import DS_FPNHead

__all__ = ['BITHead', 'Changer', 'STAHead', 'IdentityHead', 'DSIdentityHead', 
           'TinyHead', 'DS_FPNHead']
