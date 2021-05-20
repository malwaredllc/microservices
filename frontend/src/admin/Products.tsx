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


    const del = async (id: number) => {
        if (window.confirm('Are you sure you want to delete this product?')) {
            await fetch(`http://localhost:8000/api/products/${id}`, {
                method: 'DELETE'
            });

            setProducts(products.filter(
                (p: Product) => p.id !== id
            ));
        }
    }


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
                                <td>
                                    <div className="btn-group mr-2">
                                        <a href="#" className="btn btn-sm btn-outline-secondary"
                                            onClick={() => del(p.id)} 
                                        >Delete</a>
                                    </div>
                                </td>
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