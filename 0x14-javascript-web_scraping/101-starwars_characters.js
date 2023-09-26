#!/usr/bin/node

const request = require('request');

// Check if the correct number of arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: node 101-starwars_characters.js <movie-ID>');
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
      const characterUrls = movie.characters;

      // Function to fetch character names recursively and print them in order
      function fetchAndPrintCharacters (index) {
        if (index >= characterUrls.length) {
          return;
        }
        request.get(characterUrls[index], (charError, charResponse, charBody) => {
          if (charError) {
            console.error(charError);
          } else {
            const character = JSON.parse(charBody);
            console.log(character.name);
            // Fetch and print the next character
            fetchAndPrintCharacters(index + 1);
          }
        });
      }

      fetchAndPrintCharacters(0);
    } catch (parseError) {
      console.error(parseError);
    }
  }
});
