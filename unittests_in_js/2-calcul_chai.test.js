const expect = require('chai').expect;
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber', function () {
  describe('SUM', function () {
    it('rounds both numbers and adds them', function () {
      expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
    });

    it('rounds decimal parts below .5 down', function () {
      expect(calculateNumber('SUM', 1.2, 3.4)).to.equal(4);
    });

    it('rounds decimal parts equal to .5 up', function () {
      expect(calculateNumber('SUM', 1.5, 3.5)).to.equal(6);
    });
  });

  describe('SUBTRACT', function () {
    it('rounds both numbers and subtracts b from a', function () {
      expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
    });

    it('rounds the first number up before subtracting', function () {
      expect(calculateNumber('SUBTRACT', 2.6, 1.2)).to.equal(2);
    });

    it('rounds the second number up before subtracting', function () {
      expect(calculateNumber('SUBTRACT', 5.2, 2.5)).to.equal(2);
    });
  });

  describe('DIVIDE', function () {
    it('rounds both numbers and divides a by b', function () {
      expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
    });

    it('rounds the divisor before dividing', function () {
      expect(calculateNumber('DIVIDE', 8.4, 2.5)).to.equal(8 / 3);
    });

    it('returns Error when the rounded divisor is 0', function () {
      expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
    });

    it('returns Error when the divisor rounds down to 0', function () {
      expect(calculateNumber('DIVIDE', 1.4, 0.2)).to.equal('Error');
    });
  });
});
