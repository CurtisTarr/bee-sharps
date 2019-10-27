import React, { Component } from 'react';
import Table from './dataComponents/Table'
import Chart from './dataComponents/Chart'

class DataRenderer extends Component {
    constructor(props) {
        super(props);
        this.state = {};
    }

    render() {
        return (
            <div>
                <h2>DataRenderer</h2>
                <Table />
                <Chart />
            </div>
        );
    }
}

export default DataRenderer;
