import "../../css/main/Skills.css";

export default function Skills({ skillsInfo }) {
  let skills = [];
  let knowledge = [];
  let usedKnowledge = false;

  skillsInfo.forEach(element => {
    let ret = (
      <div
        className="tooltip centered skill"
        data-tooltip={element.source}
        key={"skill-" + element.name}
      >
        <li className="skill">
          <div className="value">
            {element.value}
          </div>
          <div className="skillText">
            <span className="skillName">
              {" "}{element.name}{" "}
            </span>
            <span className="skillAbility">
              {" "}{element.ability}{" "}
            </span>
          </div>
        </li>
      </div>
    );

    if (element.isKnowledge) {
      usedKnowledge = true;
      knowledge.push(ret);
    } else {
      skills.push(ret);
    }
  });

  if (usedKnowledge) {
    skills.push(<div className="skillSeparator">Knowledge</div>);
    skills.push(knowledge);
  }

  return (
    <div className="skills list-section">
      <ul>
        {skills}
      </ul>
      <div className="label">Skills</div>
    </div>
  );
}
