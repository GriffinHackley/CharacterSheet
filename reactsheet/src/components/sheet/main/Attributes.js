import "../../../css/main/Attributes.css";
import formatSource from "../../../scripts/formatSource";

export default function Attributes({ attributesInfo }) {
  let attributes = [];

  attributesInfo.forEach(element => {
    let source = formatSource(element.source);
    attributes.push(
      <li
        className="tooltip shiftedRight"
        data-tooltip={source}
        key={"attribute-" + element.name}
      >
        <div className="mod">
          <div className="abilityName">
            {element.name}
          </div>
          <div className="abilityMod">
            {element.mod}
          </div>
        </div>
        <div className="abilityScore">
          <div className="score">
            {element.score}
          </div>
        </div>
      </li>
    );
  });

  return (
    <section className="attributes">
      <div className="scores">
        <ul>
          {attributes}
        </ul>
      </div>
    </section>
  );
}
