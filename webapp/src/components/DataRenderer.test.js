import React from 'react';
import ReactDOM from 'react-dom';
import DataRenderer from './DataRenderer';

it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM.render(<DataRenderer />, div);
  ReactDOM.unmountComponentAtNode(div);
});
