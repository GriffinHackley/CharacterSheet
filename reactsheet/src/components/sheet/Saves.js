import "../../../css/sheet/main/Saves.css";
import formatSource from "../../../utils/formatSource";

export default function Saves({ savesInfo }) {
  let saves = [];

  savesInfo.forEach(element => {
    saves.push(
      <li
        className="tooltip shiftedRight"
        data-tooltip={formatSource(element.source)}
        key={"save-" + element.name}
      >
        <span className="saveName">
          {element.name}
        </span>
        <div className="value">
          {element.value}
        </div>
      </li>
    );
  });

  return (
    <div className="saves list-section">
      <ul>
        {saves}
      </ul>
      <div className="label">Saving Throws</div>
    </div>
  );
}
