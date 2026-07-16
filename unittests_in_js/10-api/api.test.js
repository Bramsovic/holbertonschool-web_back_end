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

describe('Cart page', () => {
  const url = 'http://localhost:7865/cart';

  it('returns the correct status code when id is a number', (done) => {
    request.get(`${url}/12`, (error, response) => {
      expect(error).to.equal(null);
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('returns the correct result when id is a number', (done) => {
    request.get(`${url}/12`, (error, response, body) => {
      expect(error).to.equal(null);
      expect(body).to.equal('Payment methods for cart 12');
      done();
    });
  });

  it('returns 404 when id is not a number', (done) => {
    request.get(`${url}/hello`, (error, response) => {
      expect(error).to.equal(null);
      expect(response.statusCode).to.equal(404);
      done();
    });
  });
});

describe('Available payments page', () => {
  const url = 'http://localhost:7865/available_payments';

  it('returns the correct status code', (done) => {
    request.get(url, (error, response) => {
      expect(error).to.equal(null);
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('returns the correct payment methods', (done) => {
    request.get(url, (error, response, body) => {
      expect(error).to.equal(null);
      expect(JSON.parse(body)).to.deep.equal({
        payment_methods: {
          credit_cards: true,
          paypal: false,
        },
      });
      done();
    });
  });
});

describe('Login page', () => {
  const url = 'http://localhost:7865/login';

  it('returns the correct welcome message', (done) => {
    request.post(
      {
        url,
        json: {
          userName: 'Betty',
        },
      },
      (error, response, body) => {
        expect(error).to.equal(null);
        expect(response.statusCode).to.equal(200);
        expect(body).to.equal('Welcome Betty');
        done();
      },
    );
  });
});
