#!/usr/bin/node
// Use twitter search api
// allowed modules: requests, utf8 and base64
const request = require('request');

const auth = 'Basic ' + Buffer.from(process.argv[2] + ':' +
  process.argv[3]).toString('base64');
const header = {'Authorization': auth,
  'Content-Type':
              'application/x-www-form-urlencoded;charset=UTF-8'};
const options = {
  url: 'https://api.twitter.com/oauth2/token',
  method: 'POST',
  headers: header,
  body: 'grant_type=client_credentials'
};

request(options, function (error, response, body) {
  if (!error) {
    const rJ = JSON.parse(body);
    if (rJ.token_type === 'bearer') {
      const aT = rJ.access_token;
      const headerSearch = {'Authorization': 'Bearer ' + aT};
      makeSearch(headerSearch, process.argv[4]);
    }
  }
}
);

function makeSearch (headerSearch, search) {
  const optionsSearch = {
    url: 'https://api.twitter.com/1.1/search/tweets.json',
    method: 'GET',
    headers: headerSearch,
    encoding: 'utf-8',
    qs: {'q': search, 'count': 5}
  };
  request(optionsSearch, function (error, response, body) {
    if (!error) {
      const r = JSON.parse(body);
      for (let e of r.statuses) {
        console.log('[' + e.id + '] ' + e.text + ' by ' + e.user.name);
      }
    }
  }
  );
}
