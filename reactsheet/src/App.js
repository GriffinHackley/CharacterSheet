import './App.css';
import Header from './components/header';
import Attributes from './components/attributes';
import React, { useState, useEffect } from 'react'
import axios from "axios"
import Saves from './components/saves';
import Skills from './components/skills';
import Combat from './components/combat';
import Consumables from './components/Consumables';

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
  
            const response = await axios.get('http://127.0.0.1:8000/api/characters/49');
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
            <section class="pageContainer">
                <section>
                    <Header headerInfo={character.header} ></Header>
                </section>
                <main>
                    <Attributes attributesInfo={character.attributes}></Attributes>
                    <section class="attr-applications">
                        <Saves savesInfo={character.saves}></Saves>
                        <Skills skillsInfo={character.skills}></Skills>
                    </section>
                    <section class="combatPane">
                        <Combat combatInfo={character.combat}></Combat>
                    </section>
                    <section class="rightPane">
                        <Consumables consumableInfo={character.consumables}></Consumables>
                    </section>
                </main>
            </section>
        )
    }     
}

export default App;