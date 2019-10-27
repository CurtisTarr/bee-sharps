import React from 'react';
import ReactDOM from 'react-dom';
import SimpleComponent from './SimpleComponent';

it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM.render(<SimpleComponent />, div);
  ReactDOM.unmountComponentAtNode(div);
});
