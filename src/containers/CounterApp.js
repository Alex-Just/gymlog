import React, { PropTypes } from 'react';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import * as CounterActions from '../actions/counterActions';
import Counter from '../components/Counter';

export const CounterApp = ({ value, actions }) => (
  <div>
    <Counter
      value={value}
      {...actions}
    />
  </div>
);

CounterApp.propTypes = {
  value: PropTypes.number.isRequired,
  actions: PropTypes.object.isRequired,
};

export const mapStateToProps = (state) => ({
  value: state.counter,
});

export const mapDispatchToProps = (dispatch) => ({
  actions: bindActionCreators(CounterActions, dispatch),
});

export default connect(
  mapStateToProps,
  mapDispatchToProps,
)(CounterApp);
