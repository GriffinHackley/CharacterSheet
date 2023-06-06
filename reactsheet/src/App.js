import './css/App.css';
import axios from "axios"
import React, { useState, useEffect } from 'react'

import Header from './components/Header';
import Attributes from './components/Attributes';
import Saves from './components/Saves';
import Skills from './components/Skills';
import Combat from './components/Combat';
import Consumables from './components/Consumables';
import Toggles from './components/Toggles';
import Inspiration from './components/Inspiration';
import Proficiency from './components/Proficiency';

function setColor(primary, secondary){
    let root = document.documentElement;

    root.style.setProperty('--primary-accent', primary);
    root.style.setProperty('--secondary-accent', secondary); 
}

function App() {
    const [loading, setLoading] = useState(true);
    const [character, setCharacter] = useState([]);
  
    //Get character data
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
                        <Inspiration></Inspiration>
                        <Proficiency></Proficiency>
                        <Saves savesInfo={character.saves}></Saves>
                        <Skills skillsInfo={character.skills}></Skills>
                    </section>
                    <section class="combatPane">
                        <Combat combatInfo={character.combat}></Combat>
                    </section>
                    <section class="rightPane">
                        <Consumables consumableInfo={character.consumables}></Consumables>
                        <Toggles></Toggles>
                    </section>
                </main>
            </section>
        )
    }     
}

export default App;
