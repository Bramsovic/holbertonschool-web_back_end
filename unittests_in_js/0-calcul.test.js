const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', function () {
  it('returns the sum of two rounded integers', function () {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });

  it('rounds the second argument up when its decimal part is above .5', function () {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });

  it('rounds the first argument down when its decimal part is below .5', function () {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });

  it('rounds decimal parts equal to .5 up', function () {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });

  it('rounds both arguments down when decimal parts are below .5', function () {
    assert.strictEqual(calculateNumber(1.2, 3.4), 4);
  });

  it('rounds both arguments up when decimal parts are .5 or above', function () {
    assert.strictEqual(calculateNumber(1.5, 3.5), 6);
  });

  it('handles zero values', function () {
    assert.strictEqual(calculateNumber(0, 0), 0);
  });

  it('rounds negative decimals consistently with Math.round', function () {
    assert.strictEqual(calculateNumber(-1.5, 3.7), 3);
  });
});
