import * as CounterActions from '../../actions/counterActions';
import * as types from '../../constants/actionTypes';
import expect from 'expect';


describe('CounterActions Tests', function () {
  it('returns an object with the type of INCREMENT', function () {
    expect(CounterActions.incrementCounter()).toEqual({
      type: types.INCREMENT
    });
  });

  it('returns an object with the type of DECREMENT', function () {
    expect(CounterActions.decrementCounter()).toEqual({
      type: types.DECREMENT
    });
  });
});
