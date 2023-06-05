import './App.css';
import Header from './components/header';
import React, { useState, useEffect } from 'react'
import axios from "axios"

function setColor(primary, secondary){
    let root = document.documentElement;

    root.style.setProperty('--primary-accent', primary);
    root.style.setProperty('--secondary-accent', secondary); 
}

function App() {
    const [loading, setLoading] = useState(true);
    const [character, setCharacter] = useState([]);
  
    useEffect(() => {
        const loadCharacter = async () => {
            setLoading(true);
  
            const response = await axios.get('http://127.0.0.1:8000/api/characters/52');
            setCharacter(JSON.parse(response.data));
  
            setLoading(false);
        }
  
        loadCharacter();        
    }, []);

    setColor("blue", "red")

    if(loading){
        return (
            <h4>Loading...</h4>
        )
    } else {
        return(
            
            <section>
                < Header headerInfo={character.header} ></Header>
            </section>
        )
    }     
}

export default App;
