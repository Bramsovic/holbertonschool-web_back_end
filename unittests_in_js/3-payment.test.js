const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', function () {
  it('uses Utils.calculateNumber to calculate the total', function () {
    const spy = sinon.spy(Utils, 'calculateNumber');

    try {
      sendPaymentRequestToApi(100, 20);

      sinon.assert.calledOnceWithExactly(spy, 'SUM', 100, 20);
    } finally {
      spy.restore();
    }
  });
});
