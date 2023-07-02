import "../../css/flexPanel/ProficienciesTab.css";

function makeList(allProfs, array, header){
    if(array !== 0){        
        let list = array.map(item => {
            return <p>{item}</p>
        })

        let ret = [
            <div className="proficiencyBox" key={header}>
                <h2 className="proficiencyHeader">
                    {header}
                </h2>
                {list}
            </div>
        ]

        return [...allProfs, ...ret]
    }
}

export default function ProficienciesTab({ profInfo, config }){
    let allProfs = []

    allProfs = makeList(allProfs, profInfo.skills, "Skills")
    allProfs = makeList(allProfs, profInfo.savingThrows, "Saving Throws")
    allProfs = makeList(allProfs, profInfo.armor, "Armor")
    allProfs = makeList(allProfs, profInfo.weapons, "Weapons")
    allProfs = makeList(allProfs, profInfo.tools, "Tools")
    allProfs = makeList(allProfs, profInfo.languages, "Languages")

    return (
        <section className="proficiencies">
          <div className="profContainer">
            {allProfs}
          </div>
          {/* <textarea className="profText"></textarea> */}
        </section>
    )
}