from .custom import CDDataset
from .levir_cd import LEVIR_CD_Dataset
from .s2looking import S2Looking_Dataset
from .svcd import SVCD_Dataset
from .rsipac_cd import RSIPAC_CD_Dataset
from .clcd import CLCD_Dataset
from .dsifn import DSIFN_Dataset

__all__ = ['CDDataset', 'LEVIR_CD_Dataset', 'S2Looking_Dataset', 'SVCD_Dataset',
           'RSIPAC_CD_Dataset', 'CLCD_Dataset', 'DSIFN_Dataset']
