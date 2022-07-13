# Download the zipped 201812SpotifyData data saved in the shortened (redirected) URL using curl.
# In the same step, rename file as Spotify201812.zip.
# Use curl, download and rename a single file from URL
curl -o Spotify201812.zip -L https://assets.datacamp.com/production/repositories/4180/datasets/eb1d6a36fa3039e4e00064797e1a1600d267b135/201812SpotifyData.zip

# Unzip Spotify201812.zip, delete the original zipped file, and rename the unzipped file to Spotify201812.csv to stay consistent.
# Unzip, delete, then re-name to Spotify201812.csv
unzip Spotify201812.zip && rm Spotify201812.zip
mv 201812SpotifyData.csv Spotify201812.csv

# View url_list.txt to verify content
cat url_list.txt

# Use url_list.txt and Wget to download all 3 files: Spotify201809.csv, Spotify201810.csv, and Spotify201811.csv in one step, with an upper cap download speed of 2500KB/s.
# Use Wget, limit the download rate to 2500 KB/s, download all files in url_list.txt
# Remember that by default, the download rate is in Bytes per second. In order to download in 2500KB/s, remember the unit KB/s is needed as well!
wget --limit-rate=2500k -i url_list.txt

# Take a look at all files downloaded
ls


#  -L option in LINE 4 explained
# -L, --location
              # (HTTP) If the server reports that the requested page has moved to a different location (indicated with a Location: header and a 3XX response code), this option  will  make
              # curl  redo  the  request  on the new place. If used together with -i, --include or -I, --head, headers from all requested pages will be shown. When authentication is used,
              # curl only sends its credentials to the initial host. If a redirect takes curl to a different host, it won't be able to intercept the user+password.  See  also  --location-
              # trusted on how to change this. You can limit the amount of redirects to follow by using the --max-redirs option.

              # When  curl follows a redirect and if the request is a POST, it will do the following request with a GET if the HTTP response was 301, 302, or 303. If the response code was
              # any other 3xx code, curl will re-send the following request using the same unmodified method.

              # You can tell curl to not change POST requests to GET after a 30x response by using the dedicated options for that: --post301, --post302 and --post303.

              # The method set with -X, --request overrides the method curl would otherwise select to use.
