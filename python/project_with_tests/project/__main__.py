import logging

import boto3

from jukebox_songs import JukeboxSongs

logging.basicConfig()
logging.Logger('jukebox_song_update')
logger = logging.getLogger('jukebox_song_update')
logger.setLevel(logging.INFO)

session = boto3.session.Session()
dynamo_client = session.client('dynamodb')
s3_client = session.client('s3')

bucket = "foo-bar-bucket"
file = "file/name.txt"
jukebox_songs = JukeboxSongs(
    dynamo_client=dynamo_client,
    s3_client=s3_client,
    bucket=bucket,
    key=file,
    logger=logger
)
jukebox_songs.run_update()
print('Run complete')
