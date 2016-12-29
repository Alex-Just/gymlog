import expect from "expect";
import React from "react";
import ReactDOM from "react-dom";
import TestUtils from "react-addons-test-utils";
// import Counter from "../../components/Counter";
import { GymlogApp, mapStateToProps as mapCounterAppStateToProps, mapDispatchToProps as mapCounterAppDispatchToProps } from "../../containers/GymlogApp";
import App from "../../components/App";
import { shallow } from "enzyme";
import { bindActionCreators } from 'redux';
// import * as CounterActions from '../../actions/counterActions';


// describe('<Counter />', () => {
//
//   it('should increment or decrement count after click', () => {
//
//     let count = 0;
//     const counter = TestUtils.renderIntoDocument(
//       <Counter incrementCounter={() => count++} decrementCounter={() => count--} value={count}/>
//     );
//     const counterNode = ReactDOM.findDOMNode(counter);
//
//     expect(counterNode.textContent).toEqual('Counter: 0+-');
//
//     TestUtils.Simulate.click(
//       TestUtils.scryRenderedDOMComponentsWithTag(counter, 'button')[0]
//     );
//
//     expect(count).toEqual(1);
//
//     TestUtils.Simulate.click(
//       TestUtils.scryRenderedDOMComponentsWithTag(counter, 'button')[1]
//     );
//
//     expect(count).toEqual(0);
//   });
// });

describe('<App />', () => {

  it('should render', () => {
    let count = 0;

    const app = TestUtils.renderIntoDocument(
      <App children={
        <GymlogApp
          store={{}}
          value={null}
          actions={{}}
        />
      }/>
    );

    const appNode = ReactDOM.findDOMNode(app);
    expect(appNode).toBeTruthy();
  });
});

// describe('<GymlogApp />', () => {
//
//   it('should render', () => {
//     let count = 0;
//
//     const wrapper = shallow(
//       <CounterAppUnconnected
//         store={{ counter: 0 }}
//         value={0}
//         actions={{ incrementCounter: () => count++, decrementCounter: () => count-- }}
//       />
//     );
//
//     // const util = require('util');
//     // console.log(util.inspect(wrapper, false, null));
//
//     expect(wrapper.containsMatchingElement(
//       <Counter/>
//     )).toEqual(true);
//   });
// });

// describe('<GymlogApp /> mapStateToProps', () => {
//
//   it('should mapStateToProps', () => {
//
//     expect(mapCounterAppStateToProps({ counter: 0 })).toEqual({
//       value: 0,
//     });
//   });
// });
//
// describe('<GymlogApp /> mapDispatchToProps', function () {
//
//   it('should mapDispatchToProps', () => {
//
//     expect(mapCounterAppDispatchToProps({})).toEqual({
//       actions: bindActionCreators(CounterActions, {}),
//     });
//   });
// });
