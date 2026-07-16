const { expect } = require('chai');
const request = require('request');

describe('Index page', () => {
  const url = 'http://localhost:7865';

  it('returns the correct status code', (done) => {
    request.get(url, (error, response) => {
      expect(error).to.equal(null);
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('returns the correct result', (done) => {
    request.get(url, (error, response, body) => {
      expect(error).to.equal(null);
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });

  it('returns a text/html response', (done) => {
    request.get(url, (error, response) => {
      expect(error).to.equal(null);
      expect(response.headers['content-type']).to.contain('text/html');
      done();
    });
  });
});
