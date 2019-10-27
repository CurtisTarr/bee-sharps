import React from 'react';
import DynamicTable from './dataComponents/DynamicTable'
import Chart from './dataComponents/Chart'
import { Spinner } from 'reactstrap';

function DataRenderer(props) {
    if (typeof props.columns !== 'array' && typeof props.rows !== 'object') {
        return (
            <div>
                <Spinner type="grow" color="primary" />
            </div>
        );
    } else {
        return (
            <div>
                <h2>DataRenderer</h2>
                <DynamicTable columns={props.columns} rows={props.rows} />
                <Chart />
            </div>
        );
    }
}

export default DataRenderer;
