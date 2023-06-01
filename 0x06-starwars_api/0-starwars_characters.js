#!/usr/bin/node
const request = require('request');

// Define a helper function that returns a promise for a request
const requestPromise = async (value) => 
    new Promise((resolve, reject) => {
        request(value, (error, response, data) => {
            if(error) reject(error)
            else resolve(data)
        })
    });

const endpoint = 'https://swapi-api.hbtn.io/api';
const filmId = process.argv[2];

request(`${endpoint}/films/${filmId}/`, async function (error, response, body) {
  if (error) return console.log(error);

  let characters = JSON.parse(body).characters;

  for (const character of characters) {
    let data = await requestPromise(character);
    console.log(JSON.parse(data).name);
  }
});
