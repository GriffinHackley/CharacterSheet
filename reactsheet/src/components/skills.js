import '../css/Skills.css'

export default function Skills({skillsInfo}){
    let skills = []
    let knowledge =[]
    let usedKnowledge = false

    skillsInfo.forEach(element => {
        if(element.isKnowledge){
            usedKnowledge = true
            knowledge.push(
                <div class="tooltip centered skill" data-tooltip={ element.source }>
                    <li class="skill">
                      <div class="value">
                        { element.value }
                      </div>
                      <div class="skillText">
                        <span class="skillName"> {element.name } </span>
                        <span class="skillAbility"> { element.ability } </span>
                      </div>
                    </li>
                </div>
            )
        } else {
            skills.push(
                <div class="tooltip centered skill" data-tooltip={ element.source }>
                    <li class="skill">
                      <div class="value">
                        { element.value }
                      </div>
                      <div class="skillText">
                        <span class="skillName"> {element.name } </span>
                        <span class="skillAbility"> { element.ability } </span>
                      </div>
                    </li>
                </div>
            )
        }
    });

    if(usedKnowledge){
        skills.push(
            <div class="skillSeparator">
                Knowledge
            </div>
        )
        skills.push(knowledge)
    }

    return (
        <div class="skills list-section">
            {/* <div class="skillSeparator">
                {{ section }}
            </div> */}

            <ul>
                {skills}
            </ul>
          <div class="label">
            Skills
          </div>
        </div>
    )
}