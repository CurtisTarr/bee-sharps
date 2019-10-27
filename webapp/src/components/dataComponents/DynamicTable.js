import React from 'react';
import { Table, Spinner } from 'reactstrap';

function DynamicTable(props) {
    if (typeof props.columns !== 'array' && typeof props.rows !== 'object') {
        return (
            <div>
                <Spinner type="grow" color="primary" />
            </div>
        );
    } else {
        return (
            <div>
                <Table>
                    <thead>
                        <tr>
                            {props.columns.map((column) => {
                                return (
                                    <th scope="col">{column}</th>
                                )
                            })}
                        </tr>
                    </thead>
                    <tbody>
                        {Object.entries(props.rows).map(([key, row]) => {
                            return (
                                <tr key={key}>
                                    {props.columns.map((column) => {
                                        return (
                                            <td>{row[column]}</td>
                                        )
                                    })}
                                </tr>
                            )
                        })}
                    </tbody>
                </Table>
            </div>
        );
    }
}

export default DynamicTable;
