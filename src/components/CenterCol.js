import React, { Component } from 'react';
import './CenterCol.scss';

export default class CenterCol extends Component {
  render() {
    return (
      <div className="col-md-8">
        <div className="nav-container">
          <h3>
            <span className="glyphicon glyphicon-th-large"/>&nbsp;
            <a id="dropdownMenu1" href="#" data-toggle="dropdown" className="dropdown" styleName="nav-dropdown">
              Program: My awesome standart program #1
            </a>

            &nbsp;<span className="glyphicon glyphicon-chevron-right"/>
            <a href="#" styleName="nav-dropdown">
              Day: #21
            </a>
          </h3>

          <div styleName="dropdown-menu__contents">
            <ul className="dropdown-menu" styleName="dropdown-menu">
              <li className="disabled"><a href="#">My awesome standart program #1</a></li>
              <li role="separator" className="divider"/>
              <li><a href="#">Program #2: Legs</a></li>
              <li><a href="#">Program #3: Back</a></li>
            </ul>
          </div>
        </div>

        <table className="table table-hover" styleName="main-table">
          <thead>
          <tr>
            <th>#</th>
            <th>Exercise</th>
            <th>Sets (planned)</th>
            <th>Video</th>
            <th>Note</th>
          </tr>
          </thead>
          <tbody>
          <tr>
            <td>1</td>
            <td>
              <span styleName="ex-name">Seated Stdaight-Bar Curl Superset</span>
              <a href="#" styleName="ex-controls">
                <span className="glyphicon glyphicon-pencil"/>
                Edit
              </a>

              <a href="#" styleName="ex-controls">
                <span className="glyphicon glyphicon-remove"/>
                Remove
              </a>
            </td>
            <td>
              <table className="table" styleName="table">
                <tbody>
                <tr>
                  <td>Set 1: <span styleName="input-link">12 reps</span> | <span
                    styleName="input-link">6 kg</span></td>
                </tr>
                <tr>
                  <td>Set 2: <span styleName="input-link">10 reps</span> | <span
                    styleName="input-link">6 kg</span></td>
                </tr>
                <tr>
                  <td>Set 3: <span styleName="input-link">10 reps</span> | <span
                    styleName="input-link">5 kg</span></td>
                </tr>
                <tr>
                  <td>
                    <a href="#" styleName="ex-controls"><span className="glyphicon glyphicon-plus"/> add new set</a>
                  </td>
                </tr>
                </tbody>
              </table>
            </td>
            <td>
              <iframe width="100" height="100" src="https://www.youtube.com/embed/dBogBAjK6rk?showinfo=0"/>
            </td>
            <td>
              ... blah blah blah ...
              <a href="#" styleName="ex-controls">
                <span className="glyphicon glyphicon-pencil"/>
                Edit
              </a>
            </td>
          </tr>
          <tr>
            <td>2</td>
            <td>
              <span styleName="ex-name">Seated Stdaight-Bar Curl Superset</span>
              <a href="#" styleName="ex-controls">
                <span className="glyphicon glyphicon-pencil"/>
                Edit
              </a>

              <a href="#" styleName="ex-controls">
                <span className="glyphicon glyphicon-remove"/>
                Remove
              </a>
            </td>
            <td>
              <table className="table" styleName="table">
                <tbody>
                <tr>
                  <td>Set 1: <span styleName="input-link">12 reps</span> | <span
                    styleName="input-link">6 kg</span></td>
                </tr>
                <tr>
                  <td>Set 2: <span styleName="input-link">10 reps</span> | <span
                    styleName="input-link">6 kg</span></td>
                </tr>
                <tr>
                  <td>Set 3: <span styleName="input-link">10 reps</span> | <span
                    styleName="input-link">5 kg</span></td>
                </tr>
                <tr>
                  <td>
                    <a href="#" styleName="ex-controls"><span className="glyphicon glyphicon-plus"/> add new set</a>
                  </td>
                </tr>
                </tbody>
              </table>
            </td>
            <td>
              <iframe width="100" height="100" src="https://www.youtube.com/embed/dBogBAjK6rk?showinfo=0"
              />
            </td>
            <td>
              ... blah blah blah ...
              <a href="#" styleName="ex-controls">
                <span className="glyphicon glyphicon-pencil"/>
                Edit
              </a>
            </td>
          </tr>
          <tr>
            <td>3</td>
            <td>
              <span styleName="ex-name">Seated Stdaight-Bar Curl Superset</span>
              <a href="#" styleName="ex-controls">
                <span className="glyphicon glyphicon-pencil"/>
                Edit
              </a>

              <a href="#" styleName="ex-controls">
                <span className="glyphicon glyphicon-remove"/>
                Remove
              </a>
            </td>
            <td>
              <table className="table" styleName="table">
                <tbody>
                <tr>
                  <td>Set 1: <span styleName="input-link">12 reps</span> | <span
                    styleName="input-link">6 kg</span></td>
                </tr>
                <tr>
                  <td>
                    Set 2: <span styleName="input-link">10 reps</span> |
                    <span className="hide" styleName="input-link">6 kg</span>
                    <input type="text" className="form-control" styleName="input" defaultValue="6" title=""/>
                  </td>
                </tr>
                <tr>
                  <td>Set 3: <span styleName="input-link">10 reps</span> | <span
                    styleName="input-link">5 kg</span></td>
                </tr>
                <tr>
                  <td>
                    <a href="#" styleName="ex-controls">
                      <span className="glyphicon glyphicon-plus"/> add new set
                    </a>
                  </td>
                </tr>
                </tbody>
              </table>
            </td>
            <td>
              <iframe width="100" height="100" src="https://www.youtube.com/embed/dBogBAjK6rk?showinfo=0"
              />
            </td>
            <td>
              ... blah blah blah ...
              <a href="#" styleName="ex-controls">
                <span className="glyphicon glyphicon-pencil"/>
                Edit
              </a>
            </td>
          </tr>
          </tbody>
        </table>
      </div>
    );
  }
}
