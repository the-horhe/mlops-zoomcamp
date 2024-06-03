import pandas as pd

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs):
    df = pd.read_parquet("https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-03.parquet")
    print(df.shape)

    return df


@test
def test_output(output, *args) -> None:
    assert output is not None, 'The output is undefined'
    assert isinstance(output, pd.DataFrame), f'Unexpected output format {type(output)}'
    assert len(output) > 1000000, 'Output length is too short'
