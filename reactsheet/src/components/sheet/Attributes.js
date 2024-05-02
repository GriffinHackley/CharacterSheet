import "../../css/sheet/Attributes.css";
import formatSource from "../../scripts/formatSource";
import { Checkbox, Radio } from "@mui/material";
import CircleIcon from "@mui/icons-material/Circle";
import { RadioButtonChecked, RadioButtonUnchecked } from "@mui/icons-material";

function addModAndScore(attribute) {
  let source = formatSource(attribute.source);
  return (
    <div
      className="tooltip shiftedRight"
      data-tooltip={source}
      key={"attribute-" + attribute.name}
    >
      <div className="modAndScore">
        <div className="mod">
          <div className="abilityName">
            {attribute.name}
          </div>
          <div className="abilityMod">
            {attribute.mod}
          </div>
        </div>
        <div className="abilityScore">
          <div className="score">
            {attribute.score}
          </div>
        </div>
      </div>
    </div>
  );
}

function addSave(saveInfo) {
  return (
    <div
      className="tooltip shiftedRight savingThrow"
      data-tooltip={formatSource(saveInfo.source)}
      key={"save-" + saveInfo.name}
    >
      <Checkbox
        className="proficiencyCheck"
        icon={<RadioButtonUnchecked />}
        checkedIcon={<RadioButtonChecked />}
        checked={saveInfo.proficiency}
        disabled={true}
      />
      <div className="saveValue">
        {saveInfo.value}
      </div>
      <div className="saveText">Saving Throw</div>
    </div>
  );
}

function addSkill(skillInfo) {
  return (
    <div
      className="tooltip centered skill"
      data-tooltip={formatSource(skillInfo.source)}
      key={"skill-" + skillInfo.name}
    >
      <li className="skill">
        <Checkbox
          className="proficiencyCheck"
          icon={<RadioButtonUnchecked />}
          checkedIcon={
            skillInfo.expertise ? <CircleIcon /> : <RadioButtonChecked />
          }
          checked={skillInfo.proficiency}
          disabled={true}
        />
        <div className="skillValue">
          {skillInfo.value}
        </div>
        <div className="skillName">
          {" "}{skillInfo.name}{" "}
        </div>
      </li>
    </div>
  );
}

function getAttributeColumn(attribute, saveInfo, skillsInfo) {
  let modAndScore = addModAndScore(attribute);

  let savingThrow = addSave(saveInfo);

  let skills = skillsInfo
    .filter(skill => skill.ability == attribute.name)
    .map(skill => addSkill(skill));

  let column = (
    <li className="attribute">
      {modAndScore}
      {savingThrow}
      <div className="skillSeparator">Skills</div>
      <ul className="skills">
        {skills}
      </ul>
    </li>
  );

  return column;
}

export default function Attributes({ attributesInfo, skillsInfo, savesInfo }) {
  let attributes = [];

  attributesInfo.forEach(element => {
    attributes.push(
      getAttributeColumn(element, savesInfo[element.name], skillsInfo)
    );
  });

  return (
    <section className="attributes">
      <ul className="attributes">
        {attributes}
      </ul>
    </section>
  );
}