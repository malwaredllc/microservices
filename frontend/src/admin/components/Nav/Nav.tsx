import React from 'react';

const Nav = () => {
    return (
        <nav className="navbar navbar-dark sticky-top bg-dark flex-md-nowrap p-0 shadow">
            <a className="navbar-brand col-md-3 col-lg-2 mr-0 px-3" href="/">Microservices App</a>
            <button className="navbar-toggler position-absolute d-md-none collapsed" type="button"
                    data-toggle="collapse"
                    data-target="#sidebarMenu" aria-controls="sidebarMenu" aria-expanded="false"
                    aria-label="Toggle navigation">
                <span className="navbar-toggler-icon"></span>
            </button>
        </nav>
    );
}

export default Nav;