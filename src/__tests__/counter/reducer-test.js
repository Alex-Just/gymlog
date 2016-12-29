import expect from 'expect';
import counter from '../../reducers/counter';
import * as types from '../../constants/actionTypes';

const counterReducer = counter;

const dummyTestIncrease = () => {
  const stateBefore = 1;
  const stateAfter = 2;
  const action = {
    type: types.INCREMENT,
  };

  Object.freeze(stateBefore);
  Object.freeze(action);

  expect(
    counterReducer(stateBefore, action)
  ).toEqual(stateAfter);
};

const dummyTestDecrease = () => {
  const stateBefore = 2;
  const stateAfter = 1;
  const action = {
    type: types.DECREMENT,
  };

  Object.freeze(stateBefore);
  Object.freeze(action);

  expect(
    counterReducer(stateBefore, action)
  ).toEqual(stateAfter);
};

// describe and it are global functions from mocha
describe('counterReducer Tests', function () {

  it('1 + 1 = 2', function () {
    dummyTestIncrease();
  });

  it('2 - 1 = 1', function () {
    dummyTestDecrease();
  });
});
