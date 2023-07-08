import "../../css/plan/Background.css";

export default function Background({ background }) {
  let text = [];

  for (let lines in background.feature.feature) {
    for (let line in lines) {
      text.push(
        <p>
          {background.feature.feature[line].text}
        </p>
      );
    }
  }

  let proficiencies = [];

  for (let type in background.proficiencies) {
    let profs = background.proficiencies[type];
    if (profs.length !== 0) {
      proficiencies.push(
        <div className="typeContainer">
          <b className="profType">
            {type}:
          </b>
          <p className="proficiency">
            {profs.join(", ")}
          </p>
        </div>
      );
    }
  }

  return (
    <div>
      <h2>Background</h2>
      <h4 className="backgroundName">
        {background.name}
      </h4>
      <div className="backgroundText">
        {text}
      </div>
      <div className="proficiencies">
        <h4 className="profHeader">Proficiencies</h4>
        <div className="profContent">
          {proficiencies}
        </div>
      </div>
    </div>
  );
}
