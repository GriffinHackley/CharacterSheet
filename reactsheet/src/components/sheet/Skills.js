import "../../../css/sheet/main/Skills.css";

import formatSource from "../../../utils/formatSource";

function addSkill(skillInfo) {
  return (
    <div
      className="tooltip centered skill"
      data-tooltip={formatSource(skillInfo.source)}
      key={"skill-" + skillInfo.name}
    >
      <li className="skill">
        <div className="value">
          {skillInfo.value}
        </div>
        <div className="skillText">
          <span className="skillName">
            {" "}{skillInfo.name}{" "}
          </span>
          <span className="skillAbility">
            {" "}{skillInfo.ability}{" "}
          </span>
        </div>
      </li>
    </div>
  );
}

export default function Skills({ skillsInfo }) {
  let skills = [];
  let knowledge = [];
  let usedKnowledge = false;

  skillsInfo.forEach(skill => {
    let ret = addSkill(skill);

    if (skill.isKnowledge) {
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
