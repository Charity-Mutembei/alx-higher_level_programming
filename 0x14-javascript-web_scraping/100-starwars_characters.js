#!/usr/bin/node

const request = require('request');

// Check if the correct number of arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: node 100-starwars_characters.js <movie-ID>');
  process.exit(1);
}

const movieID = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

// Send a GET request to the Star Wars API to retrieve movie details
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    try {
      const movie = JSON.parse(body);

      // Iterate through the characters and print their names
      for (const characterURL of movie.characters) {
        request.get(characterURL, (charError, charResponse, charBody) => {
          if (charError) {
            console.error(charError);
          } else {
            const character = JSON.parse(charBody);
            console.log(character.name);
          }
        });
      }
    } catch (parseError) {
      console.error(parseError);
    }
  }
});
