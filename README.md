# api
This is an API designed for [RaspApi](https://raspapi.hackclub.com/). It is built in FastAPI and hosted somewhere, i hope
## Usage
| Relative Path | Method     | Parameters                                                                                                    | Returns |
| ------------- | ------ | ---------- | ------------------------------------------------------------------------------------------------------------- |
| /jfin                      | GET          | none                 | Gets the status of my Jellyfin server via a ping.                                                                                                                                                                          |
| /time                      | GET          | none                 | Gets system time and returns it, except at 7:00 in which case it excitedly informs you that the time is 7:00.                                                                                                              |
| /where                     | GET          | none                 | Checks a schedule to determine my status and where I am (home, school, sleep).                                                                                                                                             |
| /yap                       | GET          | none                 | Gets a random text submission and returns it.                                                                                                                                                                              |
