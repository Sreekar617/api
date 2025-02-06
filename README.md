# api
This is an API designed for [RaspApi](https://raspapi.hackclub.com/). It is built in FastAPI and hosted somewhere, i hope
## Usage
| Relative Path | Method     | Parameters                                                                                                    | Returns |
| ------------- | ------ | ---------- | ------------------------------------------------------------------------------------------------------------- |
| /jfin                      | GET          | none                 | Gets the status of my Jellyfin server via a ping.                                                                                                                                                                          |
| /time                      | GET          | none                 | Gets system time and returns it, except at 7:00 in which case it excitedly informs you that the time is 7:00.                                                                                                              |
| /where                     | GET          | none                 | Checks a schedule to determine my status and where I am (home, school, sleep).                                                                                                                                             |
| /yap                       | GET          | none                 | Gets a random text submission and returns it.                                                                                                                                                                              |
| /yap                       | POST         | yap_submission="str" | Submits a string to the database, for someone to read with a GET request |

## Examples and further usage

```curl -X POST "http://127.0.0.1:8000/grades?user=user&password=password"```
For `grades`, ensure the username and password are not wrapped in the same quotes used to wrap the url
```curl -X POST "http://127.0.0.1:8000/yap?yap_submission=lowtaperfade"```
For `yap`, ensure the submission is wrapped in quotes, otherwise it can only be one word

For self deployments, please enter values for `user` and `password` in `get_grades` and fill in any other necessary keys.
