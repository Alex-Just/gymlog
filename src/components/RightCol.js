import React, { Component } from 'react';
import './RightCol.scss';

export default class RightCol extends Component {
  render() {
    return (
      <div className="col-md-2">
        <div>
      <span styleName="component">
          <b styleName="header">
              <span className="glyphicon glyphicon-calendar"/> Calendar
          </b>
      </span>

          <div styleName="empty-block">
            <i styleName="empty-text"/> Empty for now
          </div>
        </div>
      </div>
    );
  }
}
