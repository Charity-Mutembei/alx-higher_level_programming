#!/usr/bin/node

const request = require('request');

// Check if the correct number of arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: node 4-starwars_count.js <API-URL>');
  process.exit(1);
}

const apiUrl = process.argv[2];

// Send a GET request to the Star Wars API
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    try {
      const films = JSON.parse(body).results;
      const wedgeAntillesMovies = films.filter((film) =>
        film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
      );
      console.log(wedgeAntillesMovies.length);
    } catch (parseError) {
      console.error(parseError);
    }
  }
});
