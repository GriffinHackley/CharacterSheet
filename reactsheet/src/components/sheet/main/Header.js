import "../../../css/sheet/main/Header.css";

export default function Header({ headerInfo }) {
  let pathfinder = null;

  if (headerInfo.edition == "Pathfinder") {
    pathfinder = (
      <li>
        <div className="headerField">Traits</div>
        <div className="headerValue">
          {headerInfo.traits[0]}, {headerInfo.traits[1]}
        </div>
      </li>
    );
  }

  let listContent = [];

  for (let header in headerInfo) {
    let content = headerInfo[header];

    if (header == "Class and Level") {
      content = [];
      for (let cls in headerInfo["Class and Level"]) {
        content.push(
          <div className="classText">
            {cls} {headerInfo["Class and Level"][cls]}
          </div>
        );
      }
    }

    listContent.push(
      <li>
        <div className="headerValue">
          {content}
        </div>
        <b className="headerField">
          {header}
        </b>
      </li>
    );
  }

  return (
    <header>
      <section className="charname">
        <div>
          {headerInfo["Character Name"]}
        </div>
      </section>
      <section className="misc">
        <ul>
          {listContent}
        </ul>
      </section>
    </header>
  );
}
