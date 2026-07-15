const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', function () {
  describe('SUM', function () {
    it('rounds both numbers and adds them', function () {
      assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
    });

    it('rounds decimal parts below .5 down', function () {
      assert.strictEqual(calculateNumber('SUM', 1.2, 3.4), 4);
    });

    it('rounds decimal parts equal to .5 up', function () {
      assert.strictEqual(calculateNumber('SUM', 1.5, 3.5), 6);
    });
  });

  describe('SUBTRACT', function () {
    it('rounds both numbers and subtracts b from a', function () {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    });

    it('rounds the first number up before subtracting', function () {
      assert.strictEqual(calculateNumber('SUBTRACT', 2.6, 1.2), 2);
    });

    it('rounds the second number up before subtracting', function () {
      assert.strictEqual(calculateNumber('SUBTRACT', 5.2, 2.5), 2);
    });
  });

  describe('DIVIDE', function () {
    it('rounds both numbers and divides a by b', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    });

    it('rounds the divisor before dividing', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 8.4, 2.5), 8 / 3);
    });

    it('returns Error when the rounded divisor is 0', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    });

    it('returns Error when the divisor rounds down to 0', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0.2), 'Error');
    });
  });
});
