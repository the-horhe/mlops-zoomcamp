from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LinearRegression

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    # Remove extremes
    data = data[(data["duration"] >= 1) & (data["duration"] <= 60)]

    categorical = ["PULocationID", "DOLocationID"]
    numerical = ["trip_distance"]

    train_dict = data[categorical + numerical].to_dict(orient="records")

    dv = DictVectorizer()
    X_train = dv.fit_transform(train_dict)

    target = "duration"
    y_train = data[target].values

    lr = LinearRegression()
    lr.fit(X_train, y_train)

    print(lr.intercept_)

    return lr, dv


@test
def test_output(output, *args) -> None:
    assert output is not None, 'The output is undefined'
