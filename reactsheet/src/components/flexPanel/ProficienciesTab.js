import "../../css/flexPanel/ProficienciesTab.css";

function makeList(array, header){
    if(array !== 0){        
        let list = array.map(item => {
            return <p>{item}</p>
        })

        return ([
            <div className="proficiencyBox" key={header}>
                <h2 className="proficiencyHeader">
                    {header}
                </h2>
                {list}
            </div>
        ])
    }
}

export default function ProficienciesTab({ profInfo, config }){
    let allProfs = []

    allProfs = [...allProfs, ...makeList(profInfo.skills, "Skills")]
    allProfs = [...allProfs, ...makeList(profInfo.savingThrows, "Saving Throws")]
    allProfs = [...allProfs, ...makeList(profInfo.armor, "Armor")]
    allProfs = [...allProfs, ...makeList(profInfo.weapons, "Weapons")]
    allProfs = [...allProfs, ...makeList(profInfo.tools, "Tools")]
    allProfs = [...allProfs, ...makeList(profInfo.languages, "Languages")]



    return (
        <section className="proficiencies">
          <div className="profContainer">
            {allProfs}
          </div>
          {/* <textarea className="profText"></textarea> */}
        </section>
    )
}