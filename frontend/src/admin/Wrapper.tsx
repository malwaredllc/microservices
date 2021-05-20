import React, { PropsWithChildren } from 'react';
import Nav from '../components/Nav/Nav';
import Menu from '../components/Menu/Menu';
import { prependOnceListener } from 'process';

const Wrapper = (props: PropsWithChildren<any>) => {
    return (
        <div>
            <Nav/> 
        
            <div className="container-fluid">
                <div className="row">
                    <Menu/>
                        {props.children}
                </div>
            </div>
        </div>
    );
}

export default Wrapper;