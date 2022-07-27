"""UDFs for model feature engineering

File contains functions required for feature engineering"""

import numpy as np


def mapping_marital_status(x):
    """Return two series 1) informing how many adults live in given household
    and 2) with simplified marital status

    Args:
        x (data.serie): variable with marital status

    Yields:
        data.frame: with two series

    Examples:
        >>> df[['adults', 'marital_status_cleaned']] = (
        df['marital_status'].
        apply(lambda x: mapping_marital_status(x)).
        to_list())
    """
    if x in ['Single', 'Divorced', 'Widow', 'Alone']:
        val_num = 1.0
        val_verb = "single"
    elif x in ['Together', 'Married']:
        val_num = 2.0
        val_verb = "in couple"
    else:
        val_num = np.nan
        val_verb = "unknown"
    return [val_num, val_verb]
