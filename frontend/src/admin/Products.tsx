import React, { useEffect, useState } from 'react';
import Wrapper from './Wrapper';
import {Product} from '../interfaces/product';

const Products = () => {

    const [products, setProducts] = useState([]);

    useEffect( () => {
        (
            async () => {
                const response = await fetch('http://localhost:8000/api/products');
                const data = await response.json();
                setProducts(data);
            }
        )();
    }, []);

    return (
        <Wrapper>
            <div className="table-responsive">
                <table className="table table-striped">
                <thead>
                    <tr>
                        <th>#</th>
                        <th>Image</th>
                        <th>Title</th>
                        <th>Likes</th>
                        <th>Action</th>
                    </tr>
                </thead>
                <tbody>
                    {products.map((p: Product) => {
                        return (
                            <tr key={p.id}>
                                <td>{p.id}</td>
                                <td><img src={p.image} height="100"/></td>
                                <td>{p.title}</td>
                                <td>{p.likes}</td>
                                <td></td>
                            </tr>
                        );
                    })}
                </tbody>
                </table>
            </div>
        </Wrapper>
    );
}

export default Products;