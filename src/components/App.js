import React, { PropTypes, Component } from 'react';

const propTypes = {
  children: PropTypes.element.isRequired,
};

class App extends Component {

  render() {

    return (
      <main>
        {this.props.children}
      </main>
    );
  }
}

App.propTypes = propTypes;

export default App;
