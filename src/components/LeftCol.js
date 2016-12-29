import React, { Component } from 'react';
import './LeftCol.scss';

export default class CenterCol extends Component {
  render() {
    return (
      <div className="col-md-2" styleName="container">
        <div className="row">
          <div className="col-md-12" styleName="component">

            {/* User profile block */}
            <div styleName="top">
              <h1 className="text-center" styleName="header">
                GymLog
              </h1>

              <div>
                <a href="#">
                  <img styleName="avatar" src="/static/images/avatar.png" alt="Avatar"/>
                </a>
              </div>

              <div className="text-center" styleName="username">
                Ivan Petrov
              </div>
            </div>

            {/* Menu */}
            <div className="col-md-12" styleName="menu-container">
              <ul styleName="menu">

                <li styleName="menu-item">
                  <a styleName="menu-link" href="#">
                    <span className="glyphicon glyphicon-book"/> My Log
                  </a>
                </li>

                <li styleName="menu-item">
                  <a styleName="menu-link" href="#">
                    <span className="glyphicon glyphicon-user"/> Profile
                  </a>
                </li>

                <li styleName="menu-item">
                  <a styleName="menu-link" href="#">
                    <span className="glyphicon glyphicon-th-large"/> Programs
                  </a>
                </li>

                <li styleName="menu-item">
                  <a styleName="menu-link" href="#">
                    <span className="glyphicon glyphicon-plus"/> a program
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    );
  }
}
