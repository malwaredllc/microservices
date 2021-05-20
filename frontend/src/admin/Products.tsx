import React, { PropsWithChildren } from 'react';
import Wrapper from './Wrapper';

const Products = () => {
    return (
        <Wrapper>
            <div className="chartjs-size-monitor">
            <div className="chartjs-size-monitor-expand">
            <div className="chartjs-size-monitor-shrink">
            <h2>Section title</h2>

            <div className="table-responsive">
                <table className="table table-striped table-sm">
                <thead>
                    <tr>
                    <th>#</th>
                    <th>Header</th>
                    <th>Header</th>
                    <th>Header</th>
                    <th>Header</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                    <td>1,001</td>
                    <td>random</td>
                    <td>data</td>
                    <td>placeholder</td>
                    <td>text</td>
                    </tr>
                </tbody>
                </table>
            </div>
            </div>
            </div>
            </div>
        </Wrapper>
    );
}

export default Products;