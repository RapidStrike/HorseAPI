# HorseAPI 🐴

A simple, RESTful API written in Flask for fetching information related to the show My Little Pony: Friendship is Magic. URL and documentation to be added soon.

You can access the API at http://api.gollygeewhiz.xyz

## Example Response

For now, you can only retrieve episode information. Fetching <b>S4E21: Testing, Testing, 1, 2, 3</b> would return the following:

```json
{
  "air_date": "1396711800", 
  "episode": 21, 
  "season": 4,
  "synopsis": "Rainbow Dash uses unconventional methods to prepare for her test to become a member of the Wonderbolts Reserves.", 
  "title": "Testing, Testing, 1, 2, 3"
}
```

The `air_date` field is a Unix timestamp representation of when the episode first officially aired on The Hub/Discovery Family Network. A `synopsis` field may also be returned, which is just the information pulled from zap2it.tv listings.

Certain methods will also return a list of episode objects.

## Methods

### `/episodes`

Returns a list of all confirmed episodes of MLP:FIM. This will be presented in the form of an array of episodes.

### `/movies`

Returns a list of all movies for MLP:FIM. This will be presented in the form of an array of movies.

### `/all`

Returns all of the above presented in a single list.

### `/newest`

Grabs the newest upcoming episode of MLP. If there is no new episode planned, it will still return HTTP 200, but with an error rather than episode information.

### `/season/<number>`

Returns all episodes in the given season, or it returns a 400 error if the season doesn't exist or is not a number. Numeric only.

### `/season/<number>/episode/<number>`

Returns the episode as specified by the season and episode number. This will return a 400 error if any of the values aren't numbers, or if the specified episode can't be found.
