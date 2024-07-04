#!/usr/bin/env bash
set -uoe pipefail

export INPUT_FILE_PATTERN="s3://nyc-duration/in/{year:04d}-{month:02d}.parquet"
export OUTPUT_FILE_PATTERN="s3://nyc-duration/out/{year:04d}-{month:02d}.parquet"
export S3_ENDPOINT_URL=http://localhost:4566

# TODO: start/stop docker-compose
# TODO: validate data in dataset

python integration-test/generate_test_data.py 
python batch.py 2023 01

FILES_COUNT=$(aws --endpoint-url=$S3_ENDPOINT_URL s3 ls nyc-duration/out/ | wc -l)

if [ $FILES_COUNT == 1 ]
then
    exit 0
fi

echo "Test failed!"
exit 1