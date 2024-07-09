#!/usr/bin/node
/**
 * Module dependencies.
 */
const request = require('request');

/**
 * Makes an asynchronous HTTP GET request to the specified URL.
 * @param {String} url - The URL to make the request to.
 * @returns {Promise<Object>} - A promise that resolves with the parsed JSON response or rejects with an error.
 */
function makeRequest(url) {
  return new Promise((resolve, reject) => {
    request.get(url, (error, response, body) => {
      if (error) {
        reject(error); // Reject promise on request error
      } else {
        resolve(JSON.parse(body)); // Resolve promise with parsed JSON response
      }
    });
  });
}

/**
 * Main function to fetch and print Star Wars movie character names.
 */
async function main() {
  const args = process.argv;

  // Check if movie ID argument is provided
  if (args.length < 3) {
    console.error('Usage: ./script.js <movie_id>');
    return;
  }

  // Construct URL for fetching movie data
  const movieId = args[2];
  const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

  try {
    // Fetch movie data from the API
    const movie = await makeRequest(movieUrl);

    // Check if characters data exists
    if (!movie.characters || movie.characters.length === 0) {
      console.error('No character data found for this movie.');
      return;
    }

    // Fetch and print character names in order of appearance
    for (const characterUrl of movie.characters) {
      const character = await makeRequest(characterUrl);
      console.log(character.name);
    }
  } catch (error) {
    console.error('Error fetching data:', error.message);
  }
}

// Run the main function
main();
