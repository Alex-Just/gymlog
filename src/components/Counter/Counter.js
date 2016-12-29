import React, { PropTypes, Component } from 'react';

const propTypes = {
  value: PropTypes.number.isRequired,
  incrementCounter: PropTypes.func.isRequired,
  decrementCounter: PropTypes.func.isRequired,
};

class Counter extends Component {

  render() {
    const { value, incrementCounter, decrementCounter } = this.props;

    return (
      <div className="counter">
        <h1>Counter: {value}</h1>
        <button onClick={incrementCounter}>+</button>
        <button onClick={decrementCounter}>-</button>
        <hr />
      </div>
    );
  }
}

Counter.propTypes = propTypes;

export default Counter;
