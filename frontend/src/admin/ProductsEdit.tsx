import Wrapper from './Wrapper';
import {Product} from '../interfaces/product';
import {useState, useEffect, SyntheticEvent, PropsWithRef} from 'react';
import { Redirect } from 'react-router-dom';
import React from 'react';

const ProductsEdit = (props: PropsWithRef<any>) => {
    const [title, setTitle] = useState('');
    const [image, setImage] = useState('');
    const [redirect, setRedirect] = useState(false);

    useEffect( () => {
        (
            async () => {
                const response = await fetch(`http://localhost:8000/api/products/${props.match.params.id}`);
                const product: Product = await response.json();
                setTitle(product.title);
                setImage(product.image);
            }
        )();
    }, []);

    const submit = async (e: SyntheticEvent) => {
        e.preventDefault();
        
        await fetch(`http://localhost:8000/api/products/${props.match.params.id}`, {
            method: 'PUT',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                title: title, 
                image: image
            })
        });

        setRedirect(true);
    }

    if (redirect) {
        return <Redirect to='/admin/products'></Redirect>
    }

    return (
        <Wrapper>
           <form onSubmit={submit}>
                <div className="form-group">
                    <label>Title</label>
                    <input type="text" className="form-control" name="title"
                        defaultValue={title}
                        onChange={e => setTitle(e.target.value)}
                    />
                </div>
                <div className="form-group">
                    <label>Image</label>
                    <input type="text" className="form-control" name="image"
                        defaultValue={image}
                        onChange={e => setImage(e.target.value)}
                    />
                </div>
                <button className="btn btn-outline-secondary">Save</button>
            </form>
        </Wrapper>
    );
}

export default ProductsEdit;