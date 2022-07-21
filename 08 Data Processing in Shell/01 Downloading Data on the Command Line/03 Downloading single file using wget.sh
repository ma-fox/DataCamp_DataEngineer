# Fill in the two option flags
wget -c -b https://assets.datacamp.com/production/repositories/4180/datasets/eb1d6a36fa3039e4e00064797e1a1600d267b135/201812SpotifyData.zip

# Verify that the Spotify file has been downloaded
ls

# unzip *.zip
# Preview the log file
cat wget-log

# Because we asked wget to download in the background using option flag -b,
# we should always take a peak at the download log in case anything goes amiss.
