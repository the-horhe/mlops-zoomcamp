import pandas as pd
from your_first_project.utils.prepare_taxi_data import prepare_data


if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    if not isinstance(data, pd.DataFrame):
        raise RuntimeError(f'Unexpected input format: f{type(data)}')

    return prepare_data(data)


@test
def test_output(output, *args) -> None:
    assert output is not None, 'The output is undefined'
    assert len(output.columns) == 20, 'Unexpected dataframe shape'

