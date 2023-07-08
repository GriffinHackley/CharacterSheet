import "../../../css/sheet/main/Header.css";

export default function Header({ headerInfo }) {
  let pathfinder = null;

  let classes = [];
  for (let cls in headerInfo.class) {
    classes.push(
      <div>
        {cls} {headerInfo.class[cls]}
      </div>
    );
  }
  if (headerInfo.edition == "Pathfinder") {
    pathfinder = (
      <li>
        <div className="field">Traits</div>
        <div className="value">
          {headerInfo.traits[0]}, {headerInfo.traits[1]}
        </div>
      </li>
    );
  }
  return (
    <header>
      <section className="charname">
        <div>
          {headerInfo.name}
        </div>
      </section>
      <section className="misc">
        <ul>
          <li>
            <div className="field">Class & Level</div>
            <div className="value">
              {classes}
            </div>
          </li>
          <li>
            <div className="field">Background</div>
            <div className="value">
              {headerInfo.background}
            </div>
          </li>
          <li>
            <div className="field">Player Name</div>
            <div className="value">
              {headerInfo.player}
            </div>
          </li>
          <li>
            <div className="field">Race</div>
            <div className="value">
              {headerInfo.race}
            </div>
          </li>
          <li>
            <div className="field">Alignment</div>
            <div className="value">
              {headerInfo.alignment}
            </div>
          </li>
          {pathfinder}
        </ul>
      </section>
    </header>
  );
}
