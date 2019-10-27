import React, { Component } from 'react';
import './App.css';
import DataRenderer from './components/DataRenderer';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      columns: [],
      rows: {}
    };
  }

  render() {
    return (
      <div className="App">
        <DataRenderer columns={this.state.columns} rows={this.state.rows} />
      </div>
    );
  }
}

export default App;
