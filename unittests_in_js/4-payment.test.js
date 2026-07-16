const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi', function () {
  it('uses the stubbed Utils.calculateNumber result in the log message', function () {
    const stub = sinon.stub(Utils, 'calculateNumber').returns(10);
    const spy = sinon.spy(console, 'log');

    try {
      sendPaymentRequestToApi(100, 20);

      sinon.assert.calledOnceWithExactly(stub, 'SUM', 100, 20);
      sinon.assert.calledOnceWithExactly(spy, 'The total is: 10');
    } finally {
      stub.restore();
      spy.restore();
    }
  });
});
