#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Unexpected status code:', response.statusCode);
    return;
  }

  try {
    const filmData = JSON.parse(body);
    const characters = filmData.characters;

    characters.forEach(async (charUrl) => {
      const charResponse = await fetchCharacter(charUrl);
      console.log(charResponse.name);
    });
  } catch (e) {
    console.error('Error parsing JSON:', e.message);
  }
});

async function fetchCharacter(charUrl) {
  return new Promise((resolve, reject) => {
    request(charUrl, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}
