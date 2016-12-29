import React from 'react';
import { connect } from 'react-redux';
import LeftCol from '../components/LeftCol';
import CenterCol from '../components/CenterCol';
import RightCol from '../components/RightCol';
// import { bindActionCreators } from 'redux';
// import * as CounterActions from '../actions/counterActions';
// import Counter from '../components/Counter';

export const GymlogApp = () => (
  <div className="container-fluid">
    <div className="row">
      <LeftCol />
      <CenterCol />
      <RightCol />
    </div>
  </div>
);

export default connect()(GymlogApp);
